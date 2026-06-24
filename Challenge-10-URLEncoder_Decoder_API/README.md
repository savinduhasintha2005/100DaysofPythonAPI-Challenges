# ❤️ Challenge 10 - URL Encoder/Decoder API
---

# Project Structure

```
url_encoder_api/
│
├── main.py
├── requirements.txt

```

---

# Step 1: Create Project Folder

```bash
mkdir url_encoder_api
cd url_encoder_api
```

---

# Step 2: Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# Step 3: Install Dependencies

```bash
pip install fastapi uvicorn
```

Create `requirements.txt`

```txt
fastapi
uvicorn
```

Or generate automatically:

```bash
pip freeze > requirements.txt
```

---

# Step 4: Write the API

Create `main.py`

```python
from fastapi import FastAPI
from pydantic import BaseModel
from urllib.parse import quote, unquote

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
```

---

# Step 5: Run the Server

```bash
uvicorn main:app --reload
```

Server:

```
http://127.0.0.1:8000
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

# Step 6: Test the API

## 1. Encode Text

### POST

```
/encode
```

Request Body

```json
{
  "text": "https://www.google.com/search?q=python api"
}
```

Response

```json
{
  "original_text": "https://www.google.com/search?q=python api",
  "encoded_text": "https%3A//www.google.com/search%3Fq%3Dpython%20api"
}
```

---

## 2. Decode Text

### POST

```
/decode
```

Request Body

```json
{
  "text": "https%3A//www.google.com/search%3Fq%3Dpython%20api"
}
```

Response

```json
{
  "encoded_text": "https%3A//www.google.com/search%3Fq%3Dpython%20api",
  "decoded_text": "https://www.google.com/search?q=python api"
}
```

---

# Step 7: Add Error Handling (Improved Version)

```python
from fastapi import HTTPException

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
```

---

# Step 8: Test with cURL

### Encode

```bash
curl -X POST "http://127.0.0.1:8000/encode" \
-H "Content-Type: application/json" \
-d "{\"text\":\"hello world\"}"
```

Response

```json
{
  "original_text": "hello world",
  "encoded_text": "hello%20world"
}
```

---

### Decode

```bash
curl -X POST "http://127.0.0.1:8000/decode" \
-H "Content-Type: application/json" \
-d "{\"text\":\"hello%20world\"}"
```

Response

```json
{
  "encoded_text": "hello%20world",
  "decoded_text": "hello world"
}
```

