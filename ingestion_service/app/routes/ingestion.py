from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.utils import gcp_client, vector_db, document_db

router = APIRouter()


class IngestionRequest(BaseModel):
    gcp_location: str


@router.post("/ingest")
def ingest_documents(request: IngestionRequest):
    documents = gcp_client.fetch_documents(request.gcp_location)
    if not documents:
        raise HTTPException(status_code=404, detail="No documents found at the specified location.")

    vector_response = vector_db.store_documents(documents)

    document_db.store_document_data(documents)

    return {
        "status": "success",
        "documents_ingested": len(documents),
        "vector_db_response": vector_response
    }
