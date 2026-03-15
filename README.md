
# Project Overview

Large Language Models can sometimes produce **hallucinated or outdated information**.
To solve this problem, this chatbot integrates **Retrieval-Augmented Generation (RAG)** and **Live Web Search** so that responses are grounded in real data.

The system allows users to:

- Upload knowledge documents
- Ask questions based on those documents
- Fetch real-time information from the web
- Switch between concise and detailed responses

---

# Features

## Retrieval-Augmented Generation (RAG)
- Documents are split into chunks
- Text embeddings generated using **SentenceTransformers**
- Vectors stored in **FAISS**
- Relevant chunks retrieved during query time

## Live Web Search
If document context is insufficient, the chatbot performs a **real-time web search** to answer queries.

## Multiple LLM Providers
The chatbot supports:
- Groq
- OpenAI
- Google Gemini

Users can choose the provider directly from the UI.

## Response Modes
Users can toggle between:

- **Concise Mode** – Short summarized responses
- **Detailed Mode** – In-depth explanations

## Interactive UI
Built using **Streamlit** with:

- Chat interface
- File upload support
- Model selection
- Response mode toggle

---

# Project Structure

project/
│
├── config/
│   └── config.py
│
├── models/
│   ├── llm.py
│   └── embeddings.py
│
├── utils/
│   ├── document_loader.py
│   ├── vector_store.py
│   ├── web_search.py
│   └── rag_pipeline.py
│
├── app.py
├── requirements.txt
└── README.md

---

# Installation

## Clone the repository

git clone <repository-url>
cd project

## Install dependencies

pip install -r requirements.txt

---

# Environment Setup

Create a `.env` file in the root directory.

OPENAI_API_KEY=your_openai_key
GROQ_API_KEY=your_groq_key
GEMINI_API_KEY=your_gemini_key

---

# Running the Application

streamlit run app.py

The application will start in your browser.

---

# How It Works

1. **Upload Document**
   - User uploads TXT or PDF file

2. **Document Processing**
   - Text extraction
   - Chunking
   - Embedding generation
   - Storage in FAISS vector database

3. **Query Processing**
   - Retrieve relevant chunks
   - If no context found → perform web search
   - Send context + query to LLM
   - Generate final response

---

# Challenges Faced

- Handling PDF text extraction
- Managing empty embeddings and vector index errors
- Configuring multiple LLM provider APIs
- Handling LLM model deprecations
- Ensuring fallback when no documents exist

---

# Assumptions

- Uploaded documents contain readable text
- Valid API keys are provided
- Internet connection available for web search

---

# Future Improvements

- Persistent vector DB using **ChromaDB**
- Support for **DOCX, CSV, and URLs**
- Chat memory
- Better query routing between RAG and web search
- UI improvements and citations

---

# Technologies Used

- Python
- Streamlit
- FAISS
- SentenceTransformers
- Groq API
- DuckDuckGo Search

---

# Conclusion

This project demonstrates how **LLMs can be augmented with external knowledge sources** to create reliable AI systems.
Combining **RAG + Web Search + Multi‑LLM support** enables the chatbot to deliver accurate, context-aware responses.
