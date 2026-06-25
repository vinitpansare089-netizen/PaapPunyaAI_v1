"""
embedding_service.py

Purpose:
Generate vector embeddings for mythology stories.

Love-Life Translation:
Embedding = "Usne tukde kar diye."

Story ek normal text hai.
Embedding model uske meaning ko chhote numerical tukdo (vectors) mein convert kar deta hai.

Current Responsibilities:

- Load embedding model
  = Heartbreak analyzer ko ready karna.

- Convert text into vectors
  = Feelings ko numbers mein convert karna.
    ("I love you as a friend" → [0.99, 0.98, 0.97])

Future Responsibilities:

- Batch embeddings
  = Puri ex-list ko ek saath analyze karna.

- Query embeddings
  = "Kya ye wali bhi purani wali jaisi hai?"
    Similarity check.

- Embedding caching
  = Ek baar dil toot gaya to memory save kar lo.
    Baar-baar same pain calculate karne ki zarurat nahi.

Embedding = "Usne tukde kar diye."
Vector = "Tukdo ka numerical version."
Similarity Search = "Ye meri ex jaisi kyun lag rahi hai?"
Cache = "Purana trauma stored hai, instantly yaad aa jata hai."
RAG = "Purani chats padh ke jawab dena."
Chunking = "Lambi chat ko tukdo mein todna."
Vector DB = "Ex memories ka godown." 
"""

from sentence_transformers import SentenceTransformer

class EmbeddingService:

    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def create_embeddings(self, texts):

        """
            Yaha SE text lega aur encode kar raha hai vectors me ...vinit jaise usne teri baaton ke tukde kiye the.       
        """
        return self.model.encode(texts) 
    