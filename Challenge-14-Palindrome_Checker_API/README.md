# ❤️ Challenge 14 - Palindrome Checker API
---

# 📁 Project Structure

```
palindrome_checker_api/
│
├── main.py

```

---

# Step 1 Install FastAPI

```bash
pip install fastapi uvicorn
```

or

```
pip install -r requirements.txt
```

requirements.txt

```txt
fastapi
uvicorn
```

---

# Step 2 Create main.py

```python
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
```

---

# Step 3 Run the API

```bash
uvicorn main:app --reload
```

Output

```
INFO: Uvicorn running on http://127.0.0.1:8000
```

---

# Step 4 Open Swagger UI

```
http://127.0.0.1:8000/docs
```

---

# Step 5 Test the API

## Home

### GET

```
/
```

Response

```json
{
  "message": "Welcome to the Palindrome Checker API",
  "docs": "/docs"
}
```

---

## Check using POST

### Endpoint

```
POST /check
```

Request

```json
{
    "text":"racecar"
}
```

Response

```json
{
    "original_text":"racecar",
    "cleaned_text":"racecar",
    "length":7,
    "is_palindrome":true
}
```

---

### Example 2

Request

```json
{
    "text":"hello"
}
```

Response

```json
{
    "original_text":"hello",
    "cleaned_text":"hello",
    "length":5,
    "is_palindrome":false
}
```

---

### Example 3

Request

```json
{
    "text":"A man, a plan, a canal: Panama"
}
```

Response

```json
{
    "original_text":"A man, a plan, a canal: Panama",
    "cleaned_text":"amanaplanacanalpanama",
    "length":21,
    "is_palindrome":true
}
```

---

## Check using GET

```
GET /check/level
```

Response

```json
{
    "original_text":"level",
    "cleaned_text":"level",
    "length":5,
    "is_palindrome":true
}
```

---

# How It Works

Suppose the input is

```
Madam
```

### Convert to lowercase

```
madam
```

### Remove punctuation

```
madam
```

### Reverse

```
madam
```

Compare

```
madam == madam
```

Result

```
True
```

---

# Time Complexity

Cleaning string

```
O(n)
```

Reverse string

```
O(n)
```

Overall

```
O(n)
```

Space Complexity

```
O(n)
```

