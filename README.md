# Hybrid Search Application

A full-stack hybrid search application featuring **React** frontend and **FastAPI** backend, utilizing **Supabase (PostgreSQL + pgvector)** for advanced search capabilities.

## 🌟 Features

- **Hybrid Search**: Combines keyword search (Full-Text Search) and semantic search (Vector Embeddings)
- **FastAPI Backend**: High-performance Python backend with async support
- **React Frontend**: Modern, responsive UI built with Vite and TailwindCSS
- **Supabase Database**: PostgreSQL with pgvector extension for vector similarity search
- **Serverless Ready**: Optimized for Vercel deployment

## 🚀 Quick Deploy to Vercel

**Your app is 100% ready for Vercel deployment!**

### Option 1: Deploy via Vercel Dashboard (Recommended)

1. Push to GitHub:
   ```bash
   git add .
   git commit -m "Deploy to Vercel"
   git push origin main
   ```

2. Go to [vercel.com/new](https://vercel.com/new)
3. Import your repository
4. Add environment variables:
   - `DATABASE_URL`: Your Supabase connection string
   - `HF_API_KEY`: Your Hugging Face API key (optional)
5. Click "Deploy"

### Option 2: Deploy via Vercel CLI

```bash
npm install -g vercel
vercel login
vercel
```

📖 **Detailed Instructions**: See [DEPLOY_NOW.md](DEPLOY_NOW.md)

## 🛠️ Local Development

### Prerequisites

- Node.js 18+ & npm
- Python 3.9+
- Supabase account

### Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd Search_Assign
   ```

2. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your database credentials
   ```

3. **Install backend dependencies**
   ```bash
   pip install -r backend/requirements.txt
   ```

4. **Install frontend dependencies**
   ```bash
   cd frontend
   npm install
   ```

5. **Run backend**
   ```bash
   # From project root
   uvicorn backend.main:app --reload
   ```

6. **Run frontend** (in a new terminal)
   ```bash
   cd frontend
   npm run dev
   ```

7. **Access the app**
   - Frontend: http://localhost:5173
   - Backend API: http://localhost:8000
   - API Docs: http://localhost:8000/docs

## 📁 Project Structure

```
Search_Assign/
├── api/                    # Vercel serverless functions
│   └── index.py           # FastAPI serverless wrapper
├── backend/               # FastAPI backend
│   ├── main.py           # Main application
│   ├── db.py             # Database operations
│   ├── embeddings.py     # Embedding generation
│   └── requirements.txt  # Python dependencies
├── frontend/             # React frontend
│   ├── src/
│   │   └── App.jsx      # Main React component
│   ├── package.json     # Node dependencies
│   └── vite.config.js   # Vite configuration
├── vercel.json          # Vercel deployment config
├── .env.example         # Environment variables template
├── DEPLOY_NOW.md        # Quick deployment guide
└── DEPLOYMENT.md        # Detailed deployment guide
```

## 🔑 Environment Variables

Create a `.env` file in the project root:

```env
# Required: Supabase database URL
DATABASE_URL="postgresql://postgres.[PROJECT]:[PASSWORD]@[HOST]:6543/postgres"

# Optional: Hugging Face API key
HF_API_KEY="hf_xxxxxxxxxxxxx"

# Local development only
VITE_API_URL="http://localhost:8000/api"
```

## 🧪 Testing

### Test Backend API
```bash
curl http://localhost:8000/api/health
# Should return: {"status":"ok"}
```

### Test Search
```bash
curl "http://localhost:8000/api/search?q=solar%20power&mode=hybrid"
```

## 📊 Search Modes

- **Keyword**: Traditional full-text search using PostgreSQL's `ts_rank`
- **Semantic**: Vector similarity search using pgvector
- **Hybrid**: Combines both methods with weighted scoring

## 🏗️ Architecture

### Frontend
- **Framework**: React 18 with Vite
- **Styling**: TailwindCSS
- **HTTP Client**: Axios
- **Build Output**: Static files in `frontend/dist`

### Backend
- **Framework**: FastAPI
- **Database**: PostgreSQL with pgvector
- **Embeddings**: Hugging Face Inference API (sentence-transformers)
- **Deployment**: Serverless via Mangum adapter

### Database Schema
```sql
CREATE TABLE documents (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    body TEXT NOT NULL,
    embedding vector(384)  -- MiniLM-L6-v2 embeddings
);
```

## 🔧 Configuration Files

- **vercel.json**: Deployment configuration for Vercel
- **vite.config.js**: Frontend build configuration
- **.vercelignore**: Files excluded from deployment
- **requirements.txt**: Python dependencies

## 🐛 Troubleshooting

### Build Issues
- Ensure all dependencies are installed
- Check Node.js version (18+)
- Verify Python version (3.9+)

### Database Connection Issues
- Use connection pooler (port 6543)
- Verify database URL format
- Check Supabase connection limits

### Deployment Issues
- See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed troubleshooting
- Check Vercel function logs
- Verify environment variables are set

## 📚 Documentation

- [Quick Deployment Guide](DEPLOY_NOW.md) - Start here for deployment
- [Detailed Deployment Guide](DEPLOYMENT.md) - Comprehensive deployment instructions
- [Environment Variables](.env.example) - Required configuration

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is for educational/demonstration purposes.

## 🆘 Support

- Check [DEPLOYMENT.md](DEPLOYMENT.md) for deployment help
- Review Vercel logs for runtime issues
- Verify database connectivity
- Check browser console for frontend errors

## ✅ Deployment Checklist

Before deploying:
- [ ] Database is set up and accessible
- [ ] Environment variables are ready
- [ ] Code is pushed to GitHub
- [ ] Frontend builds successfully (`npm run build`)
- [ ] Backend dependencies are listed in requirements.txt

## 🎉 Success Indicators

Your deployment is successful when:
- ✅ Build completes without errors
- ✅ `/api/health` returns `{"status":"ok"}`
- ✅ Frontend loads without errors
- ✅ Search returns results
- ✅ No CORS errors in console

---

**Ready to deploy?** See [DEPLOY_NOW.md](DEPLOY_NOW.md) to get started! 🚀
