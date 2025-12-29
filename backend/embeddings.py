import os
import requests
from typing import List

HF_TOKEN = os.getenv("HF_TOKEN")

API_URL = "https://router.huggingface.co/nebius/v1/embeddings"

HEADERS = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "Content-Type": "application/json",
}

MODEL_ID = "intfloat/e5-mistral-7b-instruct"

def generate_embedding(text: str) -> List[float]:
    if not text:
        return []

    print(f"DEBUG: Generating embedding for text prefix: '{text[:20]}...'")
    print(f"DEBUG: Using Nebius embeddings API")
    print(f"DEBUG: HF_TOKEN is {'SET' if HF_TOKEN else 'MISSING'}")

    payload = {
        "model": MODEL_ID,
        "input": f"query: {text}"   # E5 requires prefix
    }

    try:
        response = requests.post(API_URL, headers=HEADERS, json=payload)
        print(f"DEBUG: Response Status: {response.status_code}")
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"DEBUG: API Request Failed: {e}")
        if response is not None:
            print(f"DEBUG: Response Content: {response.text}")
        raise

    data = response.json()

    # OpenAI-compatible response
    embedding = data["data"][0]["embedding"]

    return embedding


if __name__ == "__main__":
    try:
        vec = generate_embedding("Hybrid search is cool")
        print(f"Embedding length: {len(vec)}")
        print(f"Sample: {vec[:5]}")
    except Exception as e:
        print(f"Test failed: {e}")
