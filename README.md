# AI Search Assistant

A Retrieval-Augmented Generation (RAG) based AI search assistant that allows users to upload PDF documents and ask questions about their content.

## Features

- Upload PDF documents
- Process and index document content using FAISS and sentence transformers
- Ask questions and get AI-generated answers based on the uploaded documents
- RESTful API backend built with Flask

## Tech Stack

- **Backend**: Flask, FAISS, Sentence Transformers, Google Gemini AI
- **Frontend**: (Under development)
- **Embeddings**: all-MiniLM-L6-v2
- **LLM**: Gemini 1.5 Flash

## Setup

1. Clone the repository
2. Navigate to the backend directory
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Create a `.env` file with your Gemini API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```
5. Run the application:
   ```
   python app.py
   ```

## API Endpoints

- `GET /` - Health check
- `POST /upload` - Upload a PDF file
- `POST /ask` - Ask a question (requires PDF upload first)
- `GET /health` - Health status

## Usage

1. Start the server
2. Upload a PDF via POST to `/upload`
3. Ask questions via POST to `/ask` with JSON: `{"question": "Your question here"}`

## Project Structure

```
backend/
├── app.py          # Flask application
├── config.py       # Configuration settings
├── rag_pipeline.py # RAG pipeline implementation
├── utils.py        # Utility functions
├── requirements.txt # Python dependencies
├── test.py         # Test script
└── uploads/        # Uploaded files directory

frontend/           # Frontend application (under development)
```