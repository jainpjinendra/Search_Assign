"""
Vercel Serverless Function for FastAPI
"""
import sys
import os

# Add backend directory to path
current_dir = os.path.dirname(os.path.abspath(__file__))
backend_path = os.path.join(current_dir, '..', 'backend')
sys.path.insert(0, backend_path)

from backend.main import app
from mangum import Mangum

# Create the Mangum handler for Vercel/AWS Lambda
handler = Mangum(app, lifespan="off")
