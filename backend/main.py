from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional
import sys
import os

# Add current directory to sys.path so 'import db' works when running from root
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import db
import embeddings
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Hybrid Search Demo")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SearchResult(BaseModel):
    id: int
    title: str
    body: str
    score: float
    fts_score: Optional[float] = None
    sem_score: Optional[float] = None

# Database initialization flag
_db_initialized = False

async def ensure_db_initialized():
    """Lazy database initialization for serverless environments"""
    global _db_initialized
    if not _db_initialized:
        await db.init_db()
        _db_initialized = True

@app.get("/api/search")
async def search(
    q: str, 
    mode: str = Query("hybrid", regex="^(hybrid|semantic|keyword)$"),
    limit: int = 10
):
    await ensure_db_initialized()
    results = []
    
    if mode == "keyword":
        raw_results = await db.search_keyword(q, limit)
        # Normalize output
        for r in raw_results:
            results.append({
                "id": r['id'],
                "title": r['title'],
                "body": r['body'],
                "score": r['score'],
                "fts_score": r['score'],
                "sem_score": 0
            })
            
    elif mode == "semantic":
        emb = embeddings.generate_embedding(q)
        raw_results = await db.search_semantic(emb, limit)
        for r in raw_results:
            results.append({
                "id": r['id'],
                "title": r['title'],
                "body": r['body'],
                "score": r['score'], # This is similarity (1 - distance)
                "fts_score": 0,
                "sem_score": r['score']
            })
            
    elif mode == "hybrid":
        emb = embeddings.generate_embedding(q)
        # db.search_hybrid already returns dicts with fts_score, sem_score, hybrid_score
        raw_results = await db.search_hybrid(q, emb, limit)
        for r in raw_results:
            results.append({
                "id": r['id'],
                "title": r['title'],
                "body": r['body'],
                "score": r['hybrid_score'],
                "fts_score": r.get('fts_score', 0),
                "sem_score": r.get('sem_score', 0)
            })

    return results

@app.get("/api/health")
def health():
    return {"status": "ok"}
