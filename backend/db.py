import os
import asyncpg
from typing import List, Optional, Dict, Any
from dotenv import load_dotenv

# Load from parent directory (robust way)
import pathlib
BASE_DIR = pathlib.Path(__file__).parent.parent
load_dotenv(dotenv_path=BASE_DIR / ".env")

DATABASE_URL = os.getenv("DATABASE_URL")

async def get_db_connection():
    # statement_cache_size=0 is required for Supabase Transaction Pooler (IPv4 compatible)
    return await asyncpg.connect(DATABASE_URL, statement_cache_size=0, command_timeout=60)

async def init_db():
    conn = await get_db_connection()
    try:
        # Enable extensions
        await conn.execute("CREATE EXTENSION IF NOT EXISTS vector;")
        # await conn.execute("CREATE EXTENSION IF NOT EXISTS pgroonga;") # Using Postgres FTS for simplicity/compatibility unless pgroonga is preferred but user said "(or Postgres FTS as a fallback)"

        # Create table
        await conn.execute("""
            CREATE TABLE IF NOT EXISTS documents (
                id SERIAL PRIMARY KEY,
                title TEXT NOT NULL,
                body TEXT NOT NULL,
                embedding vector(4096)
            );
        """)
        
        # Create Indexes
        # Full text search index (using simple English dictionary for FTS)
        await conn.execute("""
            CREATE INDEX IF NOT EXISTS idx_documents_fts ON documents USING GIN (to_tsvector('english', title || ' ' || body));
        """)
        
        # Vector index

        
        print("Database initialized successfully.")
    except Exception as e:
        print(f"Error initializing DB: {e}")
    finally:
        await conn.close()

async def insert_document(title: str, body: str, embedding: List[float]):
    conn = await get_db_connection()
    try:
        await conn.execute(
            "INSERT INTO documents (title, body, embedding) VALUES ($1, $2, $3)",
            title, body, str(embedding)
        )
    finally:
        await conn.close()
        
async def search_keyword(query: str, limit: int = 10):
    conn = await get_db_connection()
    try:
        sql = """
            SELECT id, title, body, 
                   ts_rank(to_tsvector('english', title || ' ' || body), plainto_tsquery('english', $1)) as score
            FROM documents
            WHERE to_tsvector('english', title || ' ' || body) @@ plainto_tsquery('english', $1)
            ORDER BY score DESC
            LIMIT $2
        """
        rows = await conn.fetch(sql, query, limit)
        return [dict(row) for row in rows]
    finally:
        await conn.close()

async def search_semantic(embedding: List[float], limit: int = 10):
    conn = await get_db_connection()
    try:
        # Cosine distance operator <=> 
        # Convert distance to similarity: 1 - distance
        sql = """
            SELECT id, title, body, 
                   1 - (embedding <=> $1) as score
            FROM documents
            ORDER BY embedding <=> $1
            LIMIT $2
        """
        rows = await conn.fetch(sql, str(embedding), limit)
        return [dict(row) for row in rows]
    finally:
        await conn.close()

async def search_hybrid(query: str, embedding: List[float], limit: int = 10):
    conn = await get_db_connection()
    try:
        # Reciprocal Rank Fusion (RRF)
        # We fetch top matches from both strategies and fuse them.
        
        # Keyword part
        rows_kw = await conn.fetch("""
            SELECT id, title, body, 
                   ts_rank(to_tsvector('english', title || ' ' || body), plainto_tsquery('english', $1)) as text_score
            FROM documents
            WHERE to_tsvector('english', title || ' ' || body) @@ plainto_tsquery('english', $1)
            ORDER BY text_score DESC
            LIMIT $2
        """, query, limit * 2)
        
        # Semantic part
        rows_sem = await conn.fetch("""
             SELECT id, title, body, 
                   1 - (embedding <=> $1) as sem_score
            FROM documents
            ORDER BY embedding <=> $1
            LIMIT $2
        """, str(embedding), limit * 2)
        
        # RRF Merge in Python
        # score = 1 / (k + rank)
        k = 60
        scores = {}
        meta = {}
        
        # Process Keyword
        for rank, row in enumerate(rows_kw):
            id_ = row['id']
            scores[id_] = scores.get(id_, 0) + (1 / (k + rank + 1))
            meta[id_] = {**dict(row), 'fts_score': row['text_score'], 'sem_score': 0}
            
        # Process Semantic
        for rank, row in enumerate(rows_sem):
            id_ = row['id']
            scores[id_] = scores.get(id_, 0) + (1 / (k + rank + 1))
            if id_ in meta:
                meta[id_]['sem_score'] = row['sem_score']
            else:
                meta[id_] = {**dict(row), 'sem_score': row['sem_score'], 'fts_score': 0}
                
        # Sort by hybrid score
        results = []
        for id_, score in sorted(scores.items(), key=lambda x: x[1], reverse=True)[:limit]:
            item = meta[id_]
            item['hybrid_score'] = score
            results.append(item)
            
        return results

    finally:
        await conn.close()
