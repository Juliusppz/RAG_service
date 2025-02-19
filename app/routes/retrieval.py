from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.utils.chromadb_client import query_chunks
from app.utils.llm_client import generate_response

router = APIRouter()


class RetrievalRequest(BaseModel):
    query: str


@router.post("/retrieve")
def retrieve_and_generate(request: RetrievalRequest):
    if not request.query:
        raise HTTPException(status_code=400, detail="Query is required.")

    similar_chunks = query_chunks(request.query)
    response = generate_response(request.query, similar_chunks)

    return {"query": request.query, "response": response}
