from fastapi import FastAPI
from pydantic import BaseModel
from collections import Counter
import re

app = FastAPI()

# Request model
class TextRequest(BaseModel):
    text: str


def clean_and_tokenize(text: str):
    # convert to lowercase
    text = text.lower()

    # remove punctuation (keep only letters and spaces)
    words = re.findall(r'\b\w+\b', text)

    return words


@app.post("/word-frequency")
def word_frequency(request: TextRequest):
    words = clean_and_tokenize(request.text)

    freq = Counter(words)

    return dict(freq)