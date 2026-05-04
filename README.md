#  Research Paper Analyzer & Chat (RAG + LangGraph)

An end-to-end AI-powered research assistant that enables you to:

-  Analyze research papers into structured insights  
-  Chat with papers using context-aware, multi-turn conversations  
-  Retrieve accurate answers using hybrid search (BM25 + embeddings + reranking)  

Built with **FastAPI, LangGraph, LangChain, React, and Tailwind CSS**.

---

#  Features

##  Paper Analysis
Automatically extracts:
- Title  
- Authors  
- Abstract  
- Problem Statement  
- Methodology  
- Results  
- Conclusion  

---

##  Chat with Paper
- Multi-turn conversation
- Context-aware follow-ups
- Memory persistence using LangGraph
- Thread-based chat (`thread_id`)
- Grounded answers from document context

---

##  Advanced Retrieval (RAG)
- Semantic search (Chroma + embeddings(HuggingFace))
- Keyword search (BM25)
- Cross-encoder reranking
- Hybrid retrieval pipeline

---

##  Memory System
- LangGraph state management
- SQLite-based persistence
- Per-thread conversational memory

---

##  Frontend (React + Tailwind)
- ChatGPT-style UI
- Sidebar + main panel layout
- Chat + Analyze modes
- Streaming-style responses
- Clean modern design

---

#  Tech Stack

## Backend
- FastAPI
- LangGraph
- LangChain
- ChromaDB
- BM25 (rank_bm25)
- SentenceTransformers (reranker)
- SQLite (chat memory)

## Frontend
- React (Vite)
- Tailwind CSS
- Axios

---

-Demo Run
1. Install uv on your system
1. cd API
2. uv sync

Backend - 
1. CD API
2. uv run uvicorn main:app --reload

Frontend - 
1. CD API  
2. uv run streamlit run app.py

