

#  ❤️ Challenge 12 - Character Counter API
---

## 🎯 Project Goal

Create an API that accepts a text and returns:

* Total characters
* Characters without spaces
* Total words
* Total sentences
* Total lines

---

# Step 1 - Create Project Folder

```text
character-counter-api/
│
├── main.py
├── models.py

```

---

# Step 2 - Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# Step 3 - Install Packages

```bash
pip install fastapi uvicorn
```

Save dependencies

```bash
pip freeze > requirements.txt
```

---

# Step 4 - Create models.py

This file defines the request and response models.

```python
from pydantic import BaseModel


class TextRequest(BaseModel):
    text: str


class CharacterResponse(BaseModel):
    text: str
    total_characters: int
    characters_without_spaces: int
    total_words: int
    total_sentences: int
    total_lines: int
```

---

# Step 5 - Create main.py

Import packages

```python
from fastapi import FastAPI
from models import TextRequest, CharacterResponse

app = FastAPI(
    title="Character Counter API",
    description="API to count characters, words, sentences and lines.",
    version="1.0"
)
```

---

## Create Endpoint

```python
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
```

---

# Step 6 - Run Server

```bash
uvicorn main:app --reload
```

Output

```
INFO: Uvicorn running on http://127.0.0.1:8000
```

---

# Step 7 - Open Swagger UI

```
http://127.0.0.1:8000/docs
```

Click

```
POST /count
```

Click

```
Try it out
```

---

# Step 8 - Test Data

### Request

```json
{
  "text": "Hello World!\nWelcome to FastAPI.\nCharacter Counter API."
}
```

---

### Response

```json
{
  "text": "Hello World!\nWelcome to FastAPI.\nCharacter Counter API.",
  "total_characters": 57,
  "characters_without_spaces": 52,
  "total_words": 8,
  "total_sentences": 3,
  "total_lines": 3
}
```

---

# Step 9 - Test More Examples

## Example 1

Request

```json
{
  "text": "Python is awesome."
}
```

Response

```json
{
  "text": "Python is awesome.",
  "total_characters": 18,
  "characters_without_spaces": 16,
  "total_words": 3,
  "total_sentences": 1,
  "total_lines": 1
}
```

---

## Example 2

Request

```json
{
  "text": "Hi!\nHow are you?\nI'm fine."
}
```

Response

```json
{
  "text": "Hi!\nHow are you?\nI'm fine.",
  "total_characters": 27,
  "characters_without_spaces": 22,
  "total_words": 6,
  "total_sentences": 3,
  "total_lines": 3
}
```

---

# Step 10 - Project Structure

```text
character-counter-api/

│── main.py
│── models.py
│── requirements.txt
│── README.md
```

---

# How the Logic Works

### Count Characters

```python
len(text)
```

Example

```
Hello
```

Output

```
5
```

---

### Remove Spaces

```python
text.replace(" ", "")
```

Example

```
Hello World
```

becomes

```
HelloWorld
```

---

### Count Words

```python
text.split()
```

Example

```
Hello FastAPI World
```

becomes

```
["Hello","FastAPI","World"]
```

Length = 3

---

### Count Sentences

Convert

```
?
!
```

into

```
.
```

Then split using

```python
split(".")
```

---

### Count Lines

```python
splitlines()
```

Example

```
Hello
World
FastAPI
```

becomes

```
["Hello","World","FastAPI"]
```

Length = 3

---

# API Endpoint Summary

| Method | Endpoint | Description                                   |
| ------ | -------- | --------------------------------------------- |
| POST   | `/count` | Count characters, words, sentences, and lines |

---

# Expected Output

```json
{
  "text": "Hello World!",
  "total_characters": 12,
  "characters_without_spaces": 11,
  "total_words": 2,
  "total_sentences": 1,
  "total_lines": 1
}
```


