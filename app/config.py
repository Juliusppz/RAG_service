import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    chromadb_url: str = os.getenv("CHROMADB_URL", "http://chromadb:8001")
    llm_model_name: str = os.getenv("LLM_MODEL_NAME", "mistralai/Mistral-7B-Instruct")

    @property
    def api_key(self):
        try:
            with open("/run/secrets/api_key", "r") as f:
                return f.read().strip()
        except FileNotFoundError:
            return None


settings = Settings()
