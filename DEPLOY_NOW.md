# 🎯 Quick Start: Deploy to Vercel

## ✅ Your App is Now Deployment-Ready!

All configuration files have been created and optimized for Vercel deployment.

## 🚀 Two Ways to Deploy

### Method 1: Via Vercel Dashboard (Easiest - Recommended)

1. **Push your code to GitHub**
   ```powershell
   git add .
   git commit -m "Ready for Vercel deployment"
   git push origin main
   ```

2. **Go to Vercel**
   - Visit: https://vercel.com/new
   - Sign in with GitHub
   - Click "Import Git Repository"
   - Select your repository: `jainpjinendra/Search_Assign`
   - Click "Import"

3. **Configure (Important!)**
   - Framework Preset: **Other**
   - Root Directory: `./` (leave as root)
   - Build Command: (leave empty)
   - Output Directory: (leave empty)
   
4. **Add Environment Variables**
   Click "Environment Variables" and add:
   
   **Required:**
   - Name: `DATABASE_URL`
   - Value: Your Supabase connection string
     ```
     postgresql://postgres.[PROJECT]:[PASSWORD]@[HOST]:6543/postgres
     ```
   
   **Optional (if using HF API):**
   - Name: `HF_API_KEY`
   - Value: Your Hugging Face API key

5. **Deploy!**
   - Click "Deploy"
   - Wait 2-3 minutes
   - Your app will be live! 🎉

### Method 2: Via Vercel CLI

1. **Install Vercel CLI**
   ```powershell
   npm install -g vercel
   ```

2. **Login**
   ```powershell
   vercel login
   ```

3. **Deploy**
   ```powershell
   vercel
   ```
   
4. **Add Environment Variables**
   ```powershell
   vercel env add DATABASE_URL
   # Paste your database URL when prompted
   
   vercel env add HF_API_KEY
   # Paste your HF API key when prompted (optional)
   ```

5. **Deploy to Production**
   ```powershell
   vercel --prod
   ```

## 📋 What Was Changed?

### New Files Created:
- ✅ `api/index.py` - Serverless wrapper for FastAPI
- ✅ `vercel.json` - Deployment configuration
- ✅ `.vercelignore` - Files to exclude from deployment
- ✅ `DEPLOYMENT.md` - Detailed deployment guide
- ✅ `.env.example` - Environment variables template
- ✅ `deploy.bat` - Quick deployment script (Windows)

### Files Modified:
- ✅ `backend/requirements.txt` - Added `mangum` for serverless
- ✅ `backend/main.py` - Updated for serverless compatibility
- ✅ `frontend/package.json` - Added `vercel-build` script
- ✅ `frontend/src/App.jsx` - Fixed API URL for production

## 🔑 Environment Variables You Need

Get these ready before deploying:

1. **DATABASE_URL** (Required)
   - From: Supabase Dashboard → Settings → Database
   - Use: "Transaction" pooler (port 6543)
   - Format: `postgresql://postgres.[PROJECT]:[PASSWORD]@[HOST]:6543/postgres`

2. **HF_API_KEY** (Optional)
   - From: https://huggingface.co/settings/tokens
   - Only needed if using Hugging Face Inference API

## ✅ Pre-Deployment Checklist

Before deploying, make sure:

- [ ] Your code is pushed to GitHub
- [ ] Supabase database is set up and accessible
- [ ] You have your `DATABASE_URL` ready
- [ ] Database has `pgvector` extension enabled
- [ ] You have a Vercel account

## 🧪 Test After Deployment

Once deployed, test these:

1. **Health Check**
   ```
   https://your-app.vercel.app/api/health
   ```
   Should return: `{"status":"ok"}`

2. **Frontend**
   ```
   https://your-app.vercel.app
   ```
   Should load the search interface

3. **Search Functionality**
   - Try searching for "solar power"
   - Try different modes: keyword, semantic, hybrid
   - Verify results appear

## 🐛 Common Issues & Solutions

### "Build Failed"
- Check build logs in Vercel dashboard
- Verify all dependencies are listed in requirements.txt

### "API 500 Error"
- Check function logs in Vercel
- Verify DATABASE_URL is set correctly
- Ensure database is accessible from internet

### "Database Connection Failed"
- Use connection pooler (port 6543, not 5432)
- Check database credentials
- Verify database allows external connections

### "CORS Error"
- Already configured! Should work out of the box
- If issues persist, check browser console

## 📚 Additional Resources

- **Detailed Guide**: See `DEPLOYMENT.md`
- **Vercel Docs**: https://vercel.com/docs
- **Supabase Docs**: https://supabase.com/docs

## 🎉 Success!

Your app is now configured for 100% successful Vercel deployment!

**Next Step**: Choose Method 1 or Method 2 above and deploy! 🚀

---

**Questions?** Check `DEPLOYMENT.md` for detailed troubleshooting.
