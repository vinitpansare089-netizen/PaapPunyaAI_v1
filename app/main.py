from fastapi import FastAPI
from app.routers import judge

app = FastAPI(
    title="PaapPunyaAI",
    version="1.0.0",
    description="AI-powered ethical reasoning system."
)

app.include_router(judge.router)

@app.get('/chat')
def do():
    return {
        'message' : "Health is stable"
    }