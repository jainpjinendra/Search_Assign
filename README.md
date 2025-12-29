<<<<<<< HEAD
# Hybrid_Search
=======
# Hybrid_Search
# Search Application (React + FastAPI + Supabase)

This is a full-stack search application featuring a **React** frontend and a **FastAPI** backend, utilizing **Supabase (PostgreSQL)** for vector and keyword search.

## Features
- **Hybrid Search**: Combines Keyword Search (Full Text Search) and Semantic Search (Vector Embeddings).
- **FastAPI Backend**: High-performance Python backend.
- **React Frontend**: Modern user interface built with Vite.
- **Supabase Database**: Uses `pgvector` for storing and querying embeddings.

## Prerequisites
- Node.js & npm
- Python 3.11+
- Supabase Account

## Setup Instructions

### 1. Database Setup (Supabase)
1. Create a new Supabase project.
2. Enable `vector` extension in your database (handled automatically by the app on startup).
3. Get your **Connection String** (use the Transaction Pooler / IPv4 string if on a restricted network).
4. Update `backend/.env` (see below).

### 2. Backend Setup
1. Navigate to the `backend` folder? (Actually run from root usually, but let's assume root context).
   ```bash
   # Create virtual environment (optional but recommended)
   python -m venv venv
   .\venv\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   pip install fastapi uvicorn asyncpg python-dotenv
   # (Add other dependencies if any, e.g. sentence-transformers if used locally)
   ```
3. Create a `.env` file in the root directory:
   ```env
   DATABASE_URL="postgresql://postgres.[user]:[password]@[host]:6543/postgres"
   ```
4. Run the server:
   ```bash
   uvicorn backend.main:app --reload
   ```
   Server will start at `http://127.0.0.1:8000`.

### 3. Frontend Setup
1. Navigate to the `frontend` folder:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Run the development server:
   ```bash
   npm run dev
   ```
   App will be available at `http://localhost:5173`.

## Usage
1. Open the frontend URL.
2. Enter a search query (e.g., "solar power").
3. Select "Hybrid" mode for best results.


>>>>>>> 8c36416 (Initial Commit)
