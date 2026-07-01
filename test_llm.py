from services.data_service import load_stories
from services.embedding_service import EmbeddingService
from services.retrieval_service import RetrievalService
from services.prompt_service import PromptService
from services.llm_service import LLMService

#Load the stories
stories = load_stories('data/Krishna_stories.json')
# print(stories)

##Extract stories in text
texts = []

for story in stories:
    texts.append(story['story'])

### Embeddings starts form here
embeddings = EmbeddingService()

story_embeddings = embeddings.create_embeddings(texts)

###Retrieval starts from here
retrievalservice = RetrievalService(
    story_embeddings, stories
)

###FAISS indexing 
retrievalservice.create_index()

### ASK Query
query = "Should I lie to help my friend?"

### Query embedding through embedding service
query_embeddings = embeddings.create_embeddings([query])

### Retrieve stories
results = retrievalservice.search(
    query_embeddings, top_k=3
)

###Prompt service uses 
prompt_service = PromptService()

prompt = prompt_service.build_prompt(
    query,results
)

llm = LLMService(
    model_name='phi3'
)

answer = llm.generate_response(prompt)

print(answer)
