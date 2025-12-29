# 🚀 Vercel Deployment Guide

This guide will help you deploy your Hybrid Search application to Vercel successfully.

## Prerequisites

1. **Vercel Account**: Sign up at [vercel.com](https://vercel.com)
2. **Vercel CLI** (optional but recommended): `npm install -g vercel`
3. **Supabase Database**: Your PostgreSQL database must be accessible from the internet
4. **Hugging Face API Key** (if using HF Inference API for embeddings)

## 📋 Pre-Deployment Checklist

### 1. Verify Database Connection
Ensure your Supabase database is accessible:
- ✅ Database URL is correct
- ✅ Connection pooler is enabled (port 6543 recommended)
- ✅ Database has `pgvector` extension enabled
- ✅ Tables are created (run seed script if needed)

### 2. Environment Variables
You'll need these environment variables in Vercel:

| Variable | Description | Example |
|----------|-------------|---------|
| `DATABASE_URL` | PostgreSQL connection string | `postgresql://postgres.[project]:[password]@[host]:6543/postgres` |
| `HF_API_KEY` | Hugging Face API key (optional) | `hf_xxxxxxxxxxxxx` |

## 🎯 Deployment Steps

### Option 1: Deploy via Vercel Dashboard (Recommended)

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Ready for Vercel deployment"
   git push origin main
   ```

2. **Import to Vercel**
   - Go to [vercel.com/new](https://vercel.com/new)
   - Click "Import Git Repository"
   - Select your repository
   - Click "Import"

3. **Configure Project**
   - **Framework Preset**: Select "Other"
   - **Root Directory**: Leave as `./` (root)
   - **Build Command**: Leave empty (handled by vercel.json)
   - **Output Directory**: Leave empty (handled by vercel.json)

4. **Add Environment Variables**
   - Click "Environment Variables"
   - Add `DATABASE_URL` with your Supabase connection string
   - Add `HF_API_KEY` if you're using Hugging Face API
   - Make sure to add them for all environments (Production, Preview, Development)

5. **Deploy**
   - Click "Deploy"
   - Wait for the build to complete (usually 2-3 minutes)

### Option 2: Deploy via Vercel CLI

1. **Install Vercel CLI**
   ```bash
   npm install -g vercel
   ```

2. **Login to Vercel**
   ```bash
   vercel login
   ```

3. **Deploy**
   ```bash
   vercel
   ```

4. **Add Environment Variables**
   ```bash
   vercel env add DATABASE_URL
   # Paste your database URL when prompted
   
   vercel env add HF_API_KEY
   # Paste your HF API key when prompted
   ```

5. **Deploy to Production**
   ```bash
   vercel --prod
   ```

## 🔧 Configuration Details

### Frontend Configuration
- **Build Command**: `npm run build` (in frontend directory)
- **Output Directory**: `frontend/dist`
- **Framework**: Vite + React

### Backend Configuration
- **Runtime**: Python 3.9
- **Entry Point**: `api/index.py`
- **Max Duration**: 30 seconds
- **Adapter**: Mangum (FastAPI → Serverless)

### Routing
- `/api/*` → Backend (Python serverless function)
- `/*` → Frontend (Static files from dist)

## ✅ Post-Deployment Verification

1. **Check Deployment Status**
   - Go to your Vercel dashboard
   - Verify deployment is "Ready"

2. **Test API Endpoint**
   ```bash
   curl https://your-app.vercel.app/api/health
   # Should return: {"status":"ok"}
   ```

3. **Test Frontend**
   - Open `https://your-app.vercel.app` in browser
   - Try a search query
   - Verify results are returned

## 🐛 Troubleshooting

### Issue: Build Fails
**Solution**: Check build logs in Vercel dashboard
- Ensure all dependencies are in `requirements.txt` and `package.json`
- Verify Python version compatibility (3.9)

### Issue: API Returns 500 Error
**Solution**: Check function logs
- Verify `DATABASE_URL` environment variable is set correctly
- Ensure database is accessible from Vercel's servers
- Check that `pgvector` extension is enabled

### Issue: Database Connection Timeout
**Solution**: Use connection pooler
- Use port `6543` (transaction pooler) instead of `5432`
- Enable connection pooling in Supabase settings
- Consider using `asyncpg` connection pool settings

### Issue: Function Timeout
**Solution**: Optimize queries or increase timeout
- Current max duration: 30 seconds
- Optimize database queries
- Consider caching frequently accessed data
- For Pro plan, can increase to 60 seconds

### Issue: CORS Errors
**Solution**: Already configured in `backend/main.py`
- CORS is set to allow all origins (`*`)
- If you need to restrict, update `allow_origins` in main.py

## 📊 Monitoring

### View Logs
```bash
vercel logs [deployment-url]
```

### Real-time Logs
```bash
vercel logs [deployment-url] --follow
```

### Function Analytics
- Go to Vercel Dashboard → Your Project → Analytics
- Monitor function invocations, errors, and duration

## 🔄 Updating Deployment

### Automatic Deployments
- Every push to `main` branch triggers a production deployment
- Every push to other branches creates a preview deployment

### Manual Deployment
```bash
vercel --prod
```

## 🎉 Success Indicators

Your deployment is successful when:
- ✅ Build completes without errors
- ✅ `/api/health` returns `{"status":"ok"}`
- ✅ Frontend loads without errors
- ✅ Search functionality works (try "solar power" or "unit testing")
- ✅ No CORS errors in browser console

## 📝 Notes

- **Cold Starts**: First request after inactivity may be slower (2-5 seconds)
- **Serverless Limitations**: 
  - Max execution time: 30 seconds (Hobby), 60 seconds (Pro)
  - Max payload: 4.5 MB
  - Memory: 1024 MB (Hobby), 3008 MB (Pro)
- **Database**: Must be publicly accessible or use Vercel's database integration

## 🆘 Need Help?

If deployment fails:
1. Check Vercel build logs
2. Verify all environment variables are set
3. Test database connection locally
4. Review function logs for errors
5. Check [Vercel Documentation](https://vercel.com/docs)

---

**Your app should now be live at**: `https://your-project-name.vercel.app` 🎊
