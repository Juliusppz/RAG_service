import os

CHROMADB_URL = os.getenv("CHROMADB_URL", "http://chromadb:8000")
POSTGRES_URL = os.getenv("POSTGRES_URL", "postgresql://user:password@postgres:5432/document_db")
GCP_BUCKET_NAME = os.getenv("GCP_BUCKET_NAME", "your_gcp_bucket_name")
