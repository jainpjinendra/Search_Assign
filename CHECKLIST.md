# ✅ Vercel Deployment Checklist

Use this checklist to ensure 100% successful deployment.

## 📋 Pre-Deployment

### 1. Code Preparation
- [x] All configuration files created
  - [x] `api/index.py` (serverless wrapper)
  - [x] `vercel.json` (deployment config)
  - [x] `.vercelignore` (exclude files)
- [x] Backend updated for serverless
  - [x] Lazy database initialization
  - [x] Mangum adapter added
- [x] Frontend configured
  - [x] API URL set to relative path
  - [x] Build script added
- [x] Frontend build tested ✅ (Successful!)

### 2. Database Setup
- [ ] Supabase project created
- [ ] `pgvector` extension enabled
- [ ] Connection pooler enabled (port 6543)
- [ ] Database seeded with sample data
- [ ] Connection string copied

### 3. Environment Variables
- [ ] `DATABASE_URL` ready
  - Format: `postgresql://postgres.[PROJECT]:[PASSWORD]@[HOST]:6543/postgres`
- [ ] `HF_API_KEY` ready (optional)
  - Get from: https://huggingface.co/settings/tokens

### 4. Version Control
- [ ] Code committed to git
- [ ] Pushed to GitHub
- [ ] Repository is accessible

## 🚀 Deployment Steps

### Method 1: Vercel Dashboard (Recommended)

#### Step 1: Push to GitHub
```bash
git add .
git commit -m "Deploy to Vercel"
git push origin main
```
- [ ] Code pushed successfully

#### Step 2: Import to Vercel
- [ ] Go to https://vercel.com/new
- [ ] Sign in with GitHub
- [ ] Click "Import Git Repository"
- [ ] Select repository: `jainpjinendra/Search_Assign`
- [ ] Click "Import"

#### Step 3: Configure Project
- [ ] Framework Preset: **Other**
- [ ] Root Directory: `./` (leave as root)
- [ ] Build Command: (leave empty)
- [ ] Output Directory: (leave empty)

#### Step 4: Add Environment Variables
- [ ] Click "Environment Variables"
- [ ] Add `DATABASE_URL`
  - Name: `DATABASE_URL`
  - Value: [Your Supabase connection string]
  - Environments: ✅ Production ✅ Preview ✅ Development
- [ ] Add `HF_API_KEY` (optional)
  - Name: `HF_API_KEY`
  - Value: [Your HF API key]
  - Environments: ✅ Production ✅ Preview ✅ Development

#### Step 5: Deploy
- [ ] Click "Deploy" button
- [ ] Wait for build to complete (2-3 minutes)
- [ ] Deployment successful ✅

### Method 2: Vercel CLI

#### Step 1: Install CLI
```bash
npm install -g vercel
```
- [ ] Vercel CLI installed

#### Step 2: Login
```bash
vercel login
```
- [ ] Logged in successfully

#### Step 3: Deploy
```bash
vercel
```
- [ ] Preview deployment successful

#### Step 4: Add Environment Variables
```bash
vercel env add DATABASE_URL
vercel env add HF_API_KEY
```
- [ ] Environment variables added

#### Step 5: Production Deploy
```bash
vercel --prod
```
- [ ] Production deployment successful

## 🧪 Post-Deployment Testing

### 1. Health Check
- [ ] Visit: `https://your-app.vercel.app/api/health`
- [ ] Response: `{"status":"ok"}` ✅

### 2. Frontend Check
- [ ] Visit: `https://your-app.vercel.app`
- [ ] Page loads without errors ✅
- [ ] No console errors ✅

### 3. Search Functionality
- [ ] Enter search query: "solar power"
- [ ] Select mode: "Hybrid"
- [ ] Click "Search"
- [ ] Results appear ✅

### 4. Different Search Modes
- [ ] Test "Keyword" mode
- [ ] Test "Semantic" mode
- [ ] Test "Hybrid" mode
- [ ] All modes return results ✅

### 5. Error Handling
- [ ] Try empty search (should not submit)
- [ ] Try invalid query (should handle gracefully)
- [ ] Check error messages display correctly

## 📊 Monitoring

### Vercel Dashboard
- [ ] Check deployment status: "Ready"
- [ ] Review build logs (no errors)
- [ ] Check function logs (no errors)
- [ ] Monitor analytics

### Performance
- [ ] First load time < 3 seconds
- [ ] Search response time < 2 seconds
- [ ] No timeout errors

## 🐛 Troubleshooting

If deployment fails, check:

### Build Errors
- [ ] All dependencies in `requirements.txt`
- [ ] All dependencies in `package.json`
- [ ] No syntax errors in code
- [ ] Build logs in Vercel dashboard

### Runtime Errors
- [ ] Environment variables set correctly
- [ ] Database URL format correct
- [ ] Database accessible from internet
- [ ] Function logs in Vercel dashboard

### Database Errors
- [ ] Connection pooler enabled (port 6543)
- [ ] Credentials correct
- [ ] `pgvector` extension enabled
- [ ] Tables exist

### API Errors
- [ ] CORS configured (already done)
- [ ] Routes configured correctly
- [ ] Function timeout not exceeded
- [ ] Check browser console

## 📝 Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| Build fails | Check build logs, verify dependencies |
| 500 API error | Check function logs, verify DATABASE_URL |
| Database timeout | Use port 6543, enable connection pooler |
| CORS error | Already configured, check browser console |
| Function timeout | Optimize queries, check max duration (30s) |
| No results | Verify database has data, check seed script |

## ✅ Success Criteria

Your deployment is 100% successful when:

- ✅ Build completes without errors
- ✅ Deployment status is "Ready"
- ✅ `/api/health` returns `{"status":"ok"}`
- ✅ Frontend loads without errors
- ✅ Search functionality works in all modes
- ✅ No CORS errors in browser console
- ✅ Results display correctly
- ✅ No timeout errors

## 🎉 Deployment Complete!

Once all items are checked:

1. **Your app is live!** 🚀
2. **Share your URL**: `https://your-app.vercel.app`
3. **Monitor**: Check Vercel dashboard regularly
4. **Optimize**: Review analytics and performance

## 📚 Next Steps

- [ ] Set up custom domain (optional)
- [ ] Configure analytics
- [ ] Set up monitoring/alerts
- [ ] Review performance metrics
- [ ] Plan for scaling

## 🆘 Need Help?

- **Quick Guide**: [DEPLOY_NOW.md](DEPLOY_NOW.md)
- **Detailed Guide**: [DEPLOYMENT.md](DEPLOYMENT.md)
- **Vercel Docs**: https://vercel.com/docs
- **Supabase Docs**: https://supabase.com/docs

---

**Current Status**: ✅ App is configured and ready for deployment!

**Next Action**: Follow Method 1 or Method 2 above to deploy.
