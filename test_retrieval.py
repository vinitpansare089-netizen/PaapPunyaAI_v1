from services.data_service import load_stories
from services.embedding_service import EmbeddingService
from services.retrieval_service import RetrievalService

##Test krne je liye stories load kar like vo teri krti hai
stories = load_stories('data/Krishna_stories.json')

################  Embeddings section #####################

### ab sale uske dil ke tukde bhi kar de stories ko numbers me weight karke
embeddings = EmbeddingService()

texts = []

## Ek ko bhi mat chodna sb stories ke kar dena
for story in stories:
    story.texts.append(story["story"])

### Ab finally tukde ho hi gae
story_embeddings = EmbeddingService.create_embeddings(texts)

################ Retrieval section #####################

## Sari yaadon ko le le
retrieval_service = RetrievalService(story_embeddings, stories)

############### FAISS Section ####################

# Sb ko store kar le 
retrieval_service.create_index()


######### Taking query  ################

####Bhai ab new gossip le
query = "Should I lie to help my friend?"

############ Query Embedding ###########

#### aur gossip ke tukde kar de
query_embeddings = EmbeddingService.create_embedding([query])

############# Search Section ##############

## Now look in Data,, is there any purani technique that has been used before to trap you
results = 