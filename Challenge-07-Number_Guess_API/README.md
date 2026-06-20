# ❤️ Challenge 07 - Number Guess API
---
# 🚀 Day 07: Number Guess API (FastAPI)

Today you'll build a **Number Guess API** using **FastAPI**. This project teaches:

* Working with random numbers
* Query parameters
* Request validation
* API responses
* Maintaining game state
* Error handling

---

# Project Goal

Build an API where:

✅ Generate a random number (1-100)

✅ User submits guesses

✅ API tells:

* Too high
* Too low
* Correct

✅ Count attempts

✅ Reset game

---

# Project Structure

```
challenge07_number_guess_api/

│
├── main.py
├── requirements.txt
```

---

# Step 1: Create Project Folder

```bash
mkdir challenge07_number_guess_api
cd challenge07_number_guess_api
```

---

# Step 2: Create Virtual Environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# Step 3: Install FastAPI

```bash
pip install fastapi uvicorn
```

Save dependencies:

```bash
pip freeze > requirements.txt
```

---

# Step 4: Create `main.py`

```python
from fastapi import FastAPI
import random

app = FastAPI()

# Generate a secret number
secret_number = random.randint(1, 100)

# Count attempts
attempts = 0
```

---

# Step 5: Root Endpoint

```python
@app.get("/")
def home():
    return {
        "message": "Welcome to Number Guess API"
    }
```

Run:

```bash
uvicorn main:app --reload
```

Visit:

```
http://127.0.0.1:8000/
```

---

# Step 6: Create Guess Endpoint

Add:

```python
@app.get("/guess")
def guess(number: int):
    global attempts

    attempts += 1

    if number < secret_number:
        return {
            "result": "Too low",
            "attempts": attempts
        }

    elif number > secret_number:
        return {
            "result": "Too high",
            "attempts": attempts
        }

    else:
        return {
            "result": "Correct!",
            "attempts": attempts
        }
```

---

# Step 7: Test

Example:

```
http://127.0.0.1:8000/guess?number=20
```

Response:

```json
{
    "result": "Too low",
    "attempts": 1
}
```

Another:

```
http://127.0.0.1:8000/guess?number=70
```

Response:

```json
{
    "result": "Too high",
    "attempts": 2
}
```

Correct:

```json
{
    "result": "Correct!",
    "attempts": 5
}
```

---

# Step 8: Add Reset Endpoint

```python
@app.post("/reset")
def reset_game():
    global secret_number
    global attempts

    secret_number = random.randint(1, 100)
    attempts = 0

    return {
        "message": "New game started"
    }
```

---

# Step 9: Full Code

```python
from fastapi import FastAPI
import random

app = FastAPI()

secret_number = random.randint(1, 100)
attempts = 0


@app.get("/")
def home():
    return {
        "message": "Welcome to Number Guess API"
    }


@app.get("/guess")
def guess(number: int):
    global attempts

    attempts += 1

    if number < secret_number:
        return {
            "result": "Too low",
            "attempts": attempts
        }

    elif number > secret_number:
        return {
            "result": "Too high",
            "attempts": attempts
        }

    return {
        "result": "Correct!",
        "attempts": attempts
    }


@app.post("/reset")
def reset_game():
    global secret_number
    global attempts

    secret_number = random.randint(1, 100)
    attempts = 0

    return {
        "message": "New game started"
    }
```

---

# Step 10: Test with Swagger UI

Run:

```bash
uvicorn main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

Try:

* `GET /`
* `GET /guess`
* `POST /reset`

