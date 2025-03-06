import requests
from app.config import CHROMADB_URL

def store_documents(documents: list):
    try:
        response = requests.post(f"{CHROMADB_URL}/store", json={"documents": documents})
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}
