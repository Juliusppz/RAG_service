import requests
from app.config import settings


def store_chunks(chunks: list):
    try:
        response = requests.post(f"{settings.chromadb_url}/store", json={"chunks": chunks})
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}


def query_chunks(query: str, top_k: int = 3):
    try:
        response = requests.post(f"{settings.chromadb_url}/query", json={"query": query, "top_k": top_k})
        response.raise_for_status()
        return response.json().get("results", [])
    except requests.RequestException as e:
        return []

