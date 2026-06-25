from fastapi import FastAPI
from models import TextRequest, TextResponse
from pydantic import BaseModel, Field

app = FastAPI(
    title="Text Case Converter API",
    description="Convert text into different cases",
    version="1.0.0"
)


class TextRequest(BaseModel):
    text: str = Field(
        min_length=1,
        max_length=1000,
        description="Enter text to convert"
    )


@app.get("/")
def home():
    return {
        "message": "Welcome to Text Case Converter API"
    }


@app.post("/convert", response_model=TextResponse)
def convert_text(data: TextRequest):

    text = data.text

    return TextResponse(
        original=text,
        uppercase=text.upper(),
        lowercase=text.lower(),
        titlecase=text.title(),
        capitalize=text.capitalize()
    )

