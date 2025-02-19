from fastapi import FastAPI, Depends
from app.routes import ingestion, retrieval
from app.utils.auth import verify_api_key
from app.utils.metrics import generate_metrics

app = FastAPI(title="RAG Service")

# Include routers with API key dependency applied globally.
app.include_router(ingestion.router, dependencies=[Depends(verify_api_key)])
app.include_router(retrieval.router, dependencies=[Depends(verify_api_key)])


@app.get("/metrics")
def metrics():
    """Expose Prometheus metrics."""
    return generate_metrics()


# Root endpoint for health check
@app.get("/")
def read_root():
    return {"message": "RAG Service is running."}
