from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import chat


app = FastAPI(
    title="PaapPunyaAI",
    version="1.0.0",
    description="AI-powered ethical reasoning system."
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(chat.router)


@app.get("/")
def Home():
    return {
        "message": "PaapPunyaAI is Running"
    }