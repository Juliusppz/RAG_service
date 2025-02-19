from prometheus_client import Counter, generate_latest

rag_requests_total = Counter("rag_requests_total", "Total number of RAG service requests")

def generate_metrics():
    return generate_latest()
