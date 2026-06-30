from services.data_service import load_stories
from services.embedding_service import EmbeddingService
from services.retrieval_service import RetrievalService
from services.prompt_service import PromptService

#Load the stories
stories = load_stories('data/Krishna_stories.json')
# print(stories)

##yaha se embedding ka kaam start
embeddings = EmbeddingService()

text = []

for story in stories():
    text.append(story['story'])


