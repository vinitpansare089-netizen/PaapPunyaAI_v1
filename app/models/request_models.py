from pydantic import BaseModel, Field, field_validator


class ChatRequest(BaseModel):
    question: str = Field(
        ...,
        min_length=3,
        max_length=500
    )

    @field_validator("question")
    @classmethod
    def validate_question(cls, value):
        value = value.strip()

        if not value:
            raise ValueError("Question cannot be empty.")

        if not any(char.isalpha() for char in value):
            raise ValueError("Question must contain letters.")

        return value