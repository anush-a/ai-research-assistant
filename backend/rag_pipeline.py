import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import google.generativeai as genai

from config import *
from utils import *

# Lazy load models to avoid import errors
embedding_model = None
model = None

def initialize_models():
    global embedding_model, model
    if embedding_model is None:
        if not GEMINI_API_KEY:
            raise ValueError("GEMINI_API_KEY not set. Please check your .env file.")
        genai.configure(api_key=GEMINI_API_KEY)
        embedding_model = SentenceTransformer(EMBEDDING_MODEL)
        model = genai.GenerativeModel(GEMINI_MODEL)


class RAGPipeline:
    def __init__(self):
        self.index = None
        self.chunks = []
        self.embeddings = None
        initialize_models()

    def process_pdf(self, file_path):
        text = extract_text(file_path)

        self.chunks = chunk_text(
            text,
            chunk_size=CHUNK_SIZE,
            overlap=CHUNK_OVERLAP
        )

        self.embeddings = embedding_model.encode(self.chunks)

        dim = self.embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dim)
        self.index.add(np.array(self.embeddings))

    def retrieve(self, query, k=TOP_K):
        query_embedding = embedding_model.encode([query])

        distances, indices = self.index.search(
            np.array(query_embedding), k
        )

        results = []
        for i in indices[0]:
            results.append({
                "text": self.chunks[i],
                "source": f"Chunk {i}"
            })

        return results

    def generate_answer(self, query, retrieved_chunks):
        context = "\n\n".join([c["text"] for c in retrieved_chunks])

        prompt = f"""
You are an AI assistant. Answer ONLY using the context below.

Context:
{context}

Question:
{query}

Also mention sources like: (Source: Chunk X)
"""

        response = model.generate_content(prompt)

        return response.text