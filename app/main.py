from fastapi import FastAPI

app = FastAPI(
    title="PaapPunyaAI",
    version="1.0.0",
    description="AI-powered ethical reasoning system."
)

app.get('/')
def Home():
    return {
        'message': "PaapPunyaAI is Running"
    }

@app.get("/health")
def health():
    return {"status": "Healthy"}

@app.get("/about")
def about():
    return {"project": "PaapPunyaAI"}