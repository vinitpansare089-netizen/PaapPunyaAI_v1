## Data Service

What is it?

Responsible for loading knowledge data.

Why?

Separation of concerns.

Possible Interview Questions:

Q: Why not load JSON everywhere?

A: Centralized data access improves maintainability.

## Why JSON?

Problem:
Need a simple knowledge base.

Alternatives:
Database, CSV, APIs.

Decision:
JSON.

Reason:
Small dataset, easy to read, easy to modify.

Future:
PostgreSQL or document database.

## Embeddings

Problem:
Need semantic understanding.

Tool:
SentenceTransformers

Questions:

- What are embeddings?
- Why embeddings over keywords?
- What is semantic search?


## What is RAG?

Retrieval Augmented Generation.

Problem:
LLMs can hallucinate.

Solution:
Retrieve relevant knowledge before generation.

Used In:
PaapPunyaAI.

## Why Services?

The project follows Separation of Concerns.

Each service has a single responsibility.

data_service.py
- Loads datasets

embedding_service.py
- Generates embeddings

retrieval_service.py
- Retrieves relevant stories

llm_service.py
- Handles LLM inference

This improves maintainability and scalability.


## Why SentenceTransformers?

Problem:
Need semantic understanding.

Why not keyword search?
Keyword search cannot understand meaning.

Solution:
Sentence embeddings.

Model:
all-MiniLM-L6-v2

Benefits:
- Fast
- Lightweight
- Good retrieval quality
- Popular in RAG systems

Pipeline:

Text
↓
SentenceTransformer
↓
Vector Embedding
↓
FAISS Retrieval