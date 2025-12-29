"""
Vercel Serverless Function Wrapper for FastAPI
This file wraps the FastAPI app for Vercel's serverless environment
"""
import sys
import os

# Add backend directory to path
backend_path = os.path.join(os.path.dirname(__file__), '..', 'backend')
sys.path.insert(0, backend_path)

from backend.main import app
from mangum import Mangum

# Mangum adapter for AWS Lambda/Vercel
handler = Mangum(app, lifespan="off")
