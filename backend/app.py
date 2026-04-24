from flask import Flask, request, jsonify
from flask_cors import CORS
import os

from rag_pipeline import RAGPipeline

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

rag = RAGPipeline()

# ------------------ ROUTES ------------------ #

@app.route("/")
def home():
    return "RAG AI Backend Running 🚀"


@app.route("/upload", methods=["POST"])
def upload_pdf():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    try:
        rag.process_pdf(file_path)
        return jsonify({"message": "PDF processed successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/ask", methods=["POST"])
def ask_question():
    data = request.json

    if not data or "question" not in data:
        return jsonify({"error": "Question missing"}), 400

    if rag.index is None:
        return jsonify({"error": "Please upload a PDF first"}), 400

    query = data["question"]

    try:
        retrieved = rag.retrieve(query)
        answer = rag.generate_answer(query, retrieved)

        return jsonify({
            "answer": answer,
            "sources": retrieved
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "OK"})


# ------------------ RUN ------------------ #

if __name__ == "__main__":
    app.run(debug=True)