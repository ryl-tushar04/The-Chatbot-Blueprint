# Project Overview

Large Language Models can sometimes produce **hallucinated or outdated responses** when they lack external knowledge.

To solve this, the chatbot integrates:

- **RAG (Retrieval-Augmented Generation)** for document-based answers
- **Tavily Web Search** for real-time internet information

This hybrid approach ensures responses are **context-aware, grounded, and up-to-date**.

---

# Key Features

## Retrieval-Augmented Generation (RAG)

Workflow:

1. Upload a document (TXT/PDF)
2. Extract text
3. Split into chunks
4. Convert chunks into embeddings
5. Store vectors in FAISS
6. Retrieve relevant chunks during queries

Embedding model:

SentenceTransformers (all-MiniLM-L6-v2)

---

## Tavily Web Search Integration

When the chatbot cannot find relevant document context, it automatically performs **real-time web search using Tavily**.

Examples:

- weather in delhi
- latest AI news
- who is the prime minister of India

---

## Groq LLM Integration

The chatbot uses Groq's ultra-fast inference engine.

Model used:

llama-3.3-70b-versatile

Benefits:

- Low latency responses
- Strong reasoning capabilities
- Free developer access

---

# System Architecture

User Query
   ↓
Streamlit UI
   ↓
Vector Search (FAISS)
   ↓
Context Found?
   ↓          ↓
 Yes          No
  ↓            ↓
RAG Context   Tavily Web Search
       ↓
     Groq LLM
       ↓
   Final Response

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

Clone the repository

git clone <repository-url>
cd project

Install dependencies

pip install -r requirements.txt

---

# Environment Setup

Create a `.env` file locally:

GROQ_API_KEY=your_groq_key
TAVILY_API_KEY=your_tavily_key

Do **not commit `.env` to GitHub**.

---

# Running the Application

streamlit run app.py

The application will open in your browser.

---

# Deployment (Streamlit Cloud)

Add the following secrets in the Streamlit Cloud dashboard:

GROQ_API_KEY="your_key"
TAVILY_API_KEY="your_key"

---

# Technologies Used

- Python
- Streamlit
- FAISS
- SentenceTransformers
- Groq LLM
- Tavily Search API
- NumPy

---

# Future Improvements

- Persistent vector database (ChromaDB)
- Support for DOCX, CSV, URLs
- Conversation memory
- Tool-based reasoning
- Source citations

---

# Conclusion

This project demonstrates how **LLMs can be enhanced with external knowledge sources** to build reliable AI systems.

By combining:

- Retrieval-Augmented Generation
- Tavily Web Search
- Groq LLM
