from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services import question_processor, vector_db_client, openai_client

router = APIRouter()


class QueryRequest(BaseModel):
    query: str


@router.post("/query")
def process_query(request: QueryRequest):
    if not request.query:
        raise HTTPException(status_code=400, detail="Query is required.")

    subquestions = question_processor.dissect_question(request.query)
    documents = {}
    for subq in subquestions:
        docs = vector_db_client.query_documents(subq)
        documents[subq] = docs

    subanswers = {}
    for subq, docs in documents.items():
        subanswers[subq] = openai_client.generate_subanswer(subq, docs)

    final_answer = openai_client.generate_final_answer(request.query, subquestions, subanswers)

    return {
        "query": request.query,
        "subquestions": subquestions,
        "subanswers": subanswers,
        "final_answer": final_answer,
        "documents": documents
    }
