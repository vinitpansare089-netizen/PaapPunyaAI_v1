from pydantic import BaseModel
from typing import Optional


class DeityJudgment(BaseModel):

    deity: str

    response: str

    karma_score: Optional[int] = None


class ChatResponse(BaseModel):

    question: str

    judgments: list[DeityJudgment]

    final_judgment: str