from fastapi import FastAPI
from app.routes import ingestion

app = FastAPI(title="Ingestion Service")

app.include_router(ingestion.router)

@app.get("/")
def root():
    return {"message": "Ingestion Service is running."}
