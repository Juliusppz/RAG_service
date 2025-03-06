CREATE TABLE IF NOT EXISTS document_data (
    id SERIAL PRIMARY KEY,
    document_id INT UNIQUE NOT NULL,
    content TEXT NOT NULL
);
