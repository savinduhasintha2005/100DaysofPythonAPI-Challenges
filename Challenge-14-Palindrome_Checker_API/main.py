from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import re

app = FastAPI(
    title="Palindrome Checker API",
    description="Check whether a word or sentence is a palindrome.",
    version="1.0.0"
)


class TextRequest(BaseModel):
    text: str


def clean_text(text: str):
    """
    Remove spaces, punctuation and convert to lowercase.
    """
    return re.sub(r'[^a-zA-Z0-9]', '', text).lower()


def is_palindrome(text: str):
    cleaned = clean_text(text)
    return cleaned == cleaned[::-1]


@app.get("/")
def home():
    return {
        "message": "Welcome to the Palindrome Checker API",
        "docs": "/docs"
    }


@app.post("/check")
def check_palindrome(request: TextRequest):

    if request.text.strip() == "":
        raise HTTPException(
            status_code=400,
            detail="Text cannot be empty."
        )

    cleaned = clean_text(request.text)

    return {
        "original_text": request.text,
        "cleaned_text": cleaned,
        "length": len(cleaned),
        "is_palindrome": is_palindrome(request.text)
    }


@app.get("/check/{text}")
def check_palindrome_path(text: str):

    cleaned = clean_text(text)

    return {
        "original_text": text,
        "cleaned_text": cleaned,
        "length": len(cleaned),
        "is_palindrome": is_palindrome(text)
    }