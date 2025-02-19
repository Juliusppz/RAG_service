from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.utils.chunker import split_text
from app.utils.chromadb_client import store_chunks

router = APIRouter()


class IngestionRequest(BaseModel):
    text: str


@router.post("/ingest")
def ingest_text(request: IngestionRequest):
    if not request.text:
        raise HTTPException(status_code=400, detail="Text is required.")

    chunks = split_text(request.text)
    result = store_chunks(chunks)
    
    return {"status": "success", "chunks_stored": len(chunks), "result": result}
