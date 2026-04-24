import os
from dotenv import load_dotenv

load_dotenv()

# Gemini API Key (use environment variable for security)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

# Model
GEMINI_MODEL = "gemini-1.5-flash"

# Embedding model
EMBEDDING_MODEL = "all-MiniLM-L6-v2"

# Chunk settings
CHUNK_SIZE = 500
CHUNK_OVERLAP = 100

# Retrieval
TOP_K = 3