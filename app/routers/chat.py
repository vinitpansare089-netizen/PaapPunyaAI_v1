import time

from fastapi import APIRouter
from app.models.request_models import ChatRequest
from app.models.response_models import ChatResponse

from services.data_service import load_all_stories
from services.embedding_service import EmbeddingService
from services.retrieval_service import RetrievalService
from services.prompt_service import PromptService
from services.llm_service import LLMService
from services.council_service import CouncilService
from services.brahma_service import BrahmaService


# Load mythology data
stories = load_all_stories([
    "data/krishna_stories.json",
    "data/shiva_stories.json",
    "data/asura_stories.json"
])


# Services
embedding_service = EmbeddingService()

prompt_service = PromptService()

llm_service = LLMService()


# Create story texts for embeddings
texts = []

for story in stories:
    texts.append(story["story"])


# Create story embeddings
story_embeddings = embedding_service.create_embeddings(texts)


# Create retrieval service
retrieval_service = RetrievalService(
    story_embeddings,
    stories
)

retrieval_service.create_index()


# Create Brahma service
brahma_service = BrahmaService(
    llm_service
)


# Create Divine Council
council_service = CouncilService(
    llm_service,
    prompt_service,
    retrieval_service,
    embedding_service,
    brahma_service
)


router = APIRouter()


@router.post("/ask", response_model=ChatResponse)
def ask(request: ChatRequest):

    # Receive Question
    query = request.question


    # Divine Council
    start = time.time()

    council_result = council_service.conduct_council(
        query
    )

    print(
        f"Council: {time.time() - start:.2f}s"
    )


    # Return final result
    return {
        "question": query,
        "judgments": council_result["judgments"],
        "final_judgment": council_result["final_judgment"]
    }