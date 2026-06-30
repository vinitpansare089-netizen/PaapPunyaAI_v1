from services.data_service import load_stories
from services.embedding_service import EmbeddingService
from services.retrieval_service import RetrievalService
from services.prompt_service import PromptService
from services.llm_service import LLMService

stories = load_stories('data\Krishna_stories.json')

text = []

for story in stories:
    text.append(story['story'])
    