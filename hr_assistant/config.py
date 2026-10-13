# config.py
import os


class Config:
    DOCUMENTS_DIR = "resumes"
    COLLECTION_NAME = "CVs"
    PERSISTENT_DIR = "data/chromadb"
    # Embedding: modello locale di Chroma (nessuna chiave, vedi database.py)
    # Completamento
    ### ollama
    # LLM_MODEL = "llama3.2"
    # AI_API_URL = "http://localhost:11434/v1"
    # AI_API_KEY = "ollama"
    ### groq (API compatibile con OpenAI)
    LLM_MODEL = "openai/gpt-oss-120b"
    AI_API_URL = "https://api.groq.com/openai/v1"
    AI_API_KEY = os.environ.get("GROQ_API_KEY")