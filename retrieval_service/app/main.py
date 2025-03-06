from fastapi import FastAPI
from app.routes import query

app = FastAPI(title="Retrieval Service")

app.include_router(query.router)

@app.get("/")
def root():
    return {"message": "Retrieval Service is running."}
