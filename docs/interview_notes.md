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


## Embeddings

Q: What is an embedding?
A:
A dense numerical vector representation of text where semantically similar text is located closer together in vector space.

---

Q: Why use SentenceTransformers?

A:
They are optimized for semantic similarity and retrieval tasks.

---

Q: Why all-MiniLM-L6-v2?

A:
It is lightweight, fast, and provides good retrieval quality for RAG applications.

---

Q: What is the dimension of all-MiniLM-L6-v2?

A:
384 dimensions.


Interview Notes (Keep Updating)

As you requested, we'll keep documenting architecture and interview points throughout the project.

Component: FastAPI API Layer

Problem

The RAG pipeline only works through a Python script, making it inaccessible to external applications.

Solution

Expose the pipeline through a REST API using FastAPI, allowing any frontend or client to send questions over HTTP.

Why FastAPI?

High performance (built on ASGI).
Automatic request validation with Pydantic.
Interactive Swagger documentation.
Async support.
Widely adopted for ML and AI backend services.

Responsibilities

Receive HTTP requests.
Validate input.
Call existing services in sequence.
Format the response as JSON.
Handle exceptions and return appropriate HTTP status codes.

Responsibilities it should not have

Embedding generation.
Vector search.
Prompt engineering.
LLM communication.

Keeping these concerns separate improves maintainability and testability.

Possible Interview Questions

Q: Why use FastAPI for an AI backend?

A: It offers excellent performance, automatic API documentation, request validation, asynchronous support, and integrates well with Python ML libraries.

Q: Why separate services instead of writing everything in one endpoint?

A: To follow the Single Responsibility Principle. Each service focuses on one task, making the application modular, easier to test, maintain, and extend.

Q: What role does the API layer play?

A: It acts as an orchestrator. It accepts requests, validates them, invokes the business services, and returns structured responses without containing the core AI logic.