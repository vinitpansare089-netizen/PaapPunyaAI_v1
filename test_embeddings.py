"""
    You: Yaha embedding ki testing kar rahe hai jaise ... 
         usne teri testing kari thi along with many others vinit...

    Vinit: Personal kyu ho raha hai 
"""

from services.data_service import load_stories
from services.embedding_service import EmbeddingService

stories = load_stories("data/krishna_stories.json")

texts = []

for story in stories:
    texts.append(story['story'])

embedding_service = EmbeddingService()

embedding = embedding_service.create_embeddings(texts)

print(f'Stories Loaded: {len(stories)}')