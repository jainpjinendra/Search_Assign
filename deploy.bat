@echo off
echo ========================================
echo   Vercel Deployment Script
echo ========================================
echo.

REM Check if Vercel CLI is installed
where vercel >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Vercel CLI not found!
    echo Please install it first: npm install -g vercel
    echo.
    pause
    exit /b 1
)

echo [1/4] Checking git status...
git status

echo.
echo [2/4] Adding files to git...
git add .

echo.
set /p commit_msg="Enter commit message (or press Enter for default): "
if "%commit_msg%"=="" set commit_msg=Deploy to Vercel

echo [3/4] Committing changes...
git commit -m "%commit_msg%"

echo.
echo [4/4] Deploying to Vercel...
echo.
echo Choose deployment type:
echo   1. Preview deployment (test)
echo   2. Production deployment
echo.
set /p deploy_type="Enter choice (1 or 2): "

if "%deploy_type%"=="2" (
    echo.
    echo Deploying to PRODUCTION...
    vercel --prod
) else (
    echo.
    echo Deploying to PREVIEW...
    vercel
)

echo.
echo ========================================
echo   Deployment Complete!
echo ========================================
echo.
echo Check your Vercel dashboard for deployment status.
echo.
pause
