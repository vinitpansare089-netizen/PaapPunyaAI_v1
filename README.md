# PaapPunyaAI_v1

## Overview

Mythology-based RAG system using local LLMs.

## Tech Stack
- Python
- Sentence Transformers
- FAISS
- Ollama
- Phi-3

## Current Progress
✅ Knowledge Base
✅ Embeddings
✅ FAISS Retrieval
✅ LLM Integration
✅ Responces
🔄 BRAHMA Aggregate

#Architecture
Mythology Stories (JSON)
          ↓
Sentence Transformers
          ↓
Embeddings
          ↓
FAISS Vector Store
          ↓
Semantic Retrieval
          ↓
Prompt Builder
          ↓
Phi-3 / Mistral (Ollama)
          ↓
Final Response



## Docker Start Commands

- cd C:\Trinovous-Journey\PaapPunyaAI_v1

- docker ps

- docker start paappunya-dev

- docker exec -it paappunya-dev bash

- uvicorn app.main:app --host 0.0.0.0 --port 8000