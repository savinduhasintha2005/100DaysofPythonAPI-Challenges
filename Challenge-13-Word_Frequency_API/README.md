# ❤️ Challenge 12 - Word Frequency API
---

# 🚀 1. What we are building

A simple API that:

* Accepts text input
* Splits words
* Counts frequency
* Returns JSON result

Example:

### Input

```json
{
  "text": "apple banana apple orange banana apple"
}
```

### Output

```json
{
  "apple": 3,
  "banana": 2,
  "orange": 1
}
```

---

# 🧰 2. Install FastAPI + server

```bash
pip install fastapi uvicorn
```

---

# 📁 3. Project structure

```
word-frequency-api/
│── main.py
```

---

# 🧠 4. Full FastAPI Code (main.py)

```python
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
```

---

# ▶️ 5. Run the API

```bash
uvicorn main:app --reload
```

Open in browser:

```
http://127.0.0.1:8000/docs
```

FastAPI automatically gives you a Swagger UI 🎉

---

# 🧪 6. Test it

### Request:

```json
POST /word-frequency
{
  "text": "Hello world hello fastapi world"
}
```

### Response:

```json
{
  "hello": 2,
  "world": 2,
  "fastapi": 1
}
```

---

# ⚡ 7. Optional improvements (recommended)

### 1. Remove stop words

Ignore common words like “the”, “is”, “and”

```python
STOPWORDS = {"the", "is", "and", "a", "to", "in"}

words = [w for w in words if w not in STOPWORDS]
```

---

### 2. Sort by frequency

```python
return dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))
```

---

### 3. Add GET endpoint

```python
@app.get("/")
def home():
    return {"message": "Word Frequency API is running"}
```


