import psycopg2
from app.config import POSTGRES_URL

def store_document_data(documents: list):
    try:
        conn = psycopg2.connect(POSTGRES_URL)
        cursor = conn.cursor()
        cursor.executemany(
            "INSERT INTO document_data (document_id, content) VALUES (%s, %s) ON CONFLICT (document_id) DO NOTHING",
            [(doc.get("id"), doc.get("content")) for doc in documents]
        )
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print("Error storing document data:", e)
