import time

from fastapi import APIRouter
from app.models.request_models import ChatRequest
from app.models.response_models import ChatResponse

from services.data_service import load_stories, load_all_stories
from services.embedding_service import EmbeddingService
from services.retrieval_service import RetrievalService
from services.prompt_service import PromptService
from services.llm_service import LLMService
from services.council_service import CouncilService

stories = load_all_stories([
    "data/krishna_stories.json",
    "data/shiva_stories.json"
])

embedding_service = EmbeddingService()

prompt_service = PromptService()

llm_service = LLMService()


texts = []

for story in stories:
    texts.append(story["story"])

story_embeddings = embedding_service.create_embeddings(texts)

retrieval_service = RetrievalService(
    story_embeddings,
    stories
)

retrieval_service.create_index()

council_service = CouncilService(
    llm_service,
    prompt_service,
    retrieval_service,
    embedding_service
)


router = APIRouter()



    
@router.post("/ask", response_model=ChatResponse)
def ask(request: ChatRequest):

    # Receive Question
    query = request.question

    # Create Embedding
    start = time.time()

    # query_embedding = embedding_service.create_embeddings([query])

    print(f"Embedding: {time.time() - start:.2f}s")

    # Retrieve Stories
    start = time.time()

    # results = retrieval_service.search(
    #     query_embedding,
    #     top_k=3
    # )

    print(f"Retrieval: {time.time() - start:.2f}s")

    # Divine Council
    start = time.time()

    judgments = council_service.conduct_council(
        query,
    )

    print(f"Council: {time.time() - start:.2f}s")

    # Return JSON
    return {
        "question": query,
        "judgments": judgments
        # "retrieved_stories": [
        #     story["title"]
        #     for story in results
        # ]
    }