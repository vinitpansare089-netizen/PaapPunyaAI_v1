from pydantic import BaseModel


class DeityJudgment(BaseModel):
    deity: str
    response: str


class ChatResponse(BaseModel):
    question: str
    judgments: list[DeityJudgment]