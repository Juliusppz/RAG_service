import requests
from app.config import CHROMADB_URL

def query_documents(subquestion: str, top_k: int = 3):
    try:
        response = requests.post(f"{CHROMADB_URL}/query", json={"query": subquestion, "top_k": top_k})
        response.raise_for_status()
        return response.json().get("results", [])
    except Exception as e:
        return []
