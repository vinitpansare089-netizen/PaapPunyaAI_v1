import time

from fastapi import APIRouter
from app.models.request_models import ChatRequest

from services.data_service import load_stories
from services.embedding_service import EmbeddingService
from services.retrieval_service import RetrievalService
from services.prompt_service import PromptService
from services.llm_service import LLMService

stories = load_stories("data/Krishna_stories.json")

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


router = APIRouter()



    
@router.post("/ask")

def ask(request: ChatRequest):
    """
        # Receive Question

        # Create Embedding

        # Retrieve Stories

        # Build Prompt

        # Generate Answer

        # Return JSON
        """
    query = request.question

    start = time.time()

    query_embedding = embedding_service.create_embeddings([query])

    print(f"Embedding: {time.time() - start:.2f}s")

    start = time.time()

    results = retrieval_service.search(
        query_embedding,
        top_k=3
    )

    print(f"Retrieval: {time.time() - start:.2f}s")

    start = time.time()

    prompt = prompt_service.build_prompt(
        query,
        results
    )

    print(f"Prompt: {time.time() - start:.2f}s")

    start = time.time()

    answer = llm_service.generate_response(prompt)
    print(f"LLM: {time.time() - start:.2f}s")

    # return {
    #     "answer": answer
    # }

    return {
    "answer": answer,
    "retrieved_stories": [
        story["title"]
        for story in results
    ]
}