"""
## retrieval_service.py

Purpose:
Handle vector storage and similarity search.

Responsibilities:

* Create FAISS index
* Store story embeddings
* Search similar embeddings
* Return relevant stories

Inputs:

* Story embeddings
* Story metadata

Outputs:

* Most relevant stories

Dependencies:

* FAISS
* NumPy

Why Separate Service?

Embedding generation and retrieval are different concerns.

EmbeddingService creates vectors.

RetrievalService searches vectors.

"""
import faiss
import numpy as np

class RetrievalService:

    def __init__(self, embeddings, stories):## Created constructor for what will goes inside like embedding and stories
        self.embeddings = embeddings
        self.stories = stories
    
    def create_index(self):

        dimension = len(self.embeddings[0])

        index = faiss.IndexFlatL2(dimension)

        embeddings = np.array(self.embeddings, dtype= np.float32)

        index.add(embeddings)

        print("Vectors stored:", index.ntotal)
