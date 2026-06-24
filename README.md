# 📄 PDF AI Chatbot 

An AI-powered chatbot that allows users to upload PDF files and ask questions. The system uses Retrieval-Augmented Generation (RAG) with embeddings and a local LLM (Ollama).

---

## 🚀 Features

- Upload multiple PDFs
- Extract text using PyPDF
- Chunk documents for better retrieval
- Semantic search using ChromaDB
- Embedding generation using SentenceTransformers
- AI answers using Ollama LLM
- Source-based response tracking

---

## 🏗️ Architecture

User → Streamlit UI  
↓  
FastAPI Backend  
↓  
PDF Processing (PyPDF)  
↓  
Chunking (Custom logic)  
↓  
Embeddings (SentenceTransformers)  
↓  
Vector DB (ChromaDB)  
↓  
Retriever (Similarity Search)  
↓  
LLM (Ollama)  
↓  
Final Answer returned to UI

---

## ⚙️ Setup Instructions

### 1. Clone repository
```bash
git clone https://github.com/laavanya19/pdf-chatbot.git
cd pdf-chatbot
