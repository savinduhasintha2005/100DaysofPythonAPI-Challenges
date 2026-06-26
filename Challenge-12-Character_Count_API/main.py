from fastapi import FastAPI
from models import TextRequest, CharacterResponse

app = FastAPI(
    title="Character Counter API",
    description="API to count characters, words, sentences and lines.",
    version="1.0"
)

@app.post("/count", response_model=CharacterResponse)
def count_characters(request: TextRequest):

    text = request.text

    total_characters = len(text)

    characters_without_spaces = len(text.replace(" ", ""))

    words = text.split()

    total_words = len(words)

    sentences = [s for s in text.replace("?", ".").replace("!", ".").split(".") if s.strip()]

    total_sentences = len(sentences)

    lines = text.splitlines()

    total_lines = len(lines) if lines else 1

    return CharacterResponse(
        text=text,
        total_characters=total_characters,
        characters_without_spaces=characters_without_spaces,
        total_words=total_words,
        total_sentences=total_sentences,
        total_lines=total_lines
    )