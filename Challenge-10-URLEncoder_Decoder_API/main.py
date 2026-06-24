from fastapi import FastAPI
from pydantic import BaseModel
from urllib.parse import quote, unquote
from fastapi import HTTPException

app = FastAPI(
    title="URL Encoder/Decoder API",
    description="Encode and decode URLs using Python",
    version="1.0.0"
)


# Request model
class TextRequest(BaseModel):
    text: str


# Home endpoint
@app.get("/")
def home():
    return {
        "message": "Welcome to URL Encoder/Decoder API"
    }


# Encode endpoint
@app.post("/encode")
def encode_url(data: TextRequest):
    encoded = quote(data.text)

    return {
        "original_text": data.text,
        "encoded_text": encoded
    }


# Decode endpoint
@app.post("/decode")
def decode_url(data: TextRequest):
    decoded = unquote(data.text)

    return {
        "encoded_text": data.text,
        "decoded_text": decoded
    }


@app.post("/encode")
def encode_url(data: TextRequest):
    if not data.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")

    return {
        "original_text": data.text,
        "encoded_text": quote(data.text)
    }


@app.post("/decode")
def decode_url(data: TextRequest):
    if not data.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")

    return {
        "encoded_text": data.text,
        "decoded_text": unquote(data.text)
    }