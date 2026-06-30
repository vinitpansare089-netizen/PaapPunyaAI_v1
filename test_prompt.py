from services.data_service import load_stories
from services.embedding_service import EmbeddingService
from services.retrieval_service import RetrievalService
from services.prompt_service import PromptService

#Load the stories
stories = load_stories('data/Krishna_stories.json')
# print(stories)

##Extract stories in text
text = []

for story in stories():
    text.append(story['story'])

### Embeddings starts form here
story_embeddings = EmbeddingService.create_embeddings(text)



