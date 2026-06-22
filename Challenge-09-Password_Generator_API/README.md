# ❤️ Challenge 09 - Password Generator API
---

# Project Structure

```
password_generator_api/
│
├── main.py
├── requirements.txt
```

---

# Step 1: Create Project Folder

```bash
mkdir password_generator_api
cd password_generator_api
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

Save dependencies:

```bash
pip freeze > requirements.txt
```

---

# Step 4: Create `main.py`

```python
from fastapi import FastAPI
import secrets
import string

app = FastAPI(
    title="Password Generator API",
    description="Generate secure passwords",
    version="1.0"
)
```

---

# Step 5: Create Basic Password Generator

Add:

```python
def generate_password(length=12):
    characters = string.ascii_letters + string.digits
    password = ''.join(
        secrets.choice(characters)
        for _ in range(length)
    )
    return password
```

---

# Step 6: Create API Endpoint

```python
@app.get("/")
def home():
    return {"message": "Password Generator API"}
```

Create password endpoint:

```python
@app.get("/generate")
def generate(length: int = 12):
    password = generate_password(length)
    return {
        "password": password
    }
```

---

# Step 7: Run the API

```bash
uvicorn main:app --reload
```

Server:

```
http://127.0.0.1:8000
```

---

# Step 8: Test Endpoint

Open:

```
http://127.0.0.1:8000/generate
```

Example response:

```json
{
  "password": "w9R4P2nX7LkA"
}
```

Custom length:

```
http://127.0.0.1:8000/generate?length=20
```

Response:

```json
{
  "password": "u9B3Mp6Qk4AzWr8Lx5Nf"
}
```

---

# Step 9: Add More Options

Import:

```python
import string
```

Update generator:

```python
def generate_password(
    length=12,
    uppercase=True,
    lowercase=True,
    digits=True,
    symbols=False
):
    characters = ""

    if uppercase:
        characters += string.ascii_uppercase

    if lowercase:
        characters += string.ascii_lowercase

    if digits:
        characters += string.digits

    if symbols:
        characters += string.punctuation

    password = ''.join(
        secrets.choice(characters)
        for _ in range(length)
    )

    return password
```

---

# Step 10: Update Endpoint

```python
@app.get("/generate")
def generate(
        length: int = 12,
        uppercase: bool = True,
        lowercase: bool = True,
        digits: bool = True,
        symbols: bool = False
):
    password = generate_password(
        length,
        uppercase,
        lowercase,
        digits,
        symbols
    )

    return {
        "password": password,
        "length": length
    }
```

---

# Example URLs

### Default

```
http://127.0.0.1:8000/generate
```

### 16-character password

```
http://127.0.0.1:8000/generate?length=16
```

### Include symbols

```
http://127.0.0.1:8000/generate?length=20&symbols=true
```

### Numbers only

```
http://127.0.0.1:8000/generate?uppercase=false&lowercase=false&digits=true
```

---

# Step 11: Add Validation

```python
from fastapi import HTTPException
```

Inside endpoint:

```python
if length < 4 or length > 100:
    raise HTTPException(
        status_code=400,
        detail="Password length must be between 4 and 100"
    )
```

Prevent empty character set:

```python
if not any([uppercase, lowercase, digits, symbols]):
    raise HTTPException(
        status_code=400,
        detail="At least one character type must be enabled"
    )
```

---

# Step 12: Complete Code

```python
from fastapi import FastAPI, HTTPException
import secrets
import string

app = FastAPI(
    title="Password Generator API",
    version="1.0"
)

def generate_password(length, uppercase, lowercase, digits, symbols):
    characters = ""

    if uppercase:
        characters += string.ascii_uppercase

    if lowercase:
        characters += string.ascii_lowercase

    if digits:
        characters += string.digits

    if symbols:
        characters += string.punctuation

    return ''.join(
        secrets.choice(characters)
        for _ in range(length)
    )

@app.get("/")
def home():
    return {"message": "Password Generator API"}

@app.get("/generate")
def generate(
        length: int = 12,
        uppercase: bool = True,
        lowercase: bool = True,
        digits: bool = True,
        symbols: bool = False):

    if length < 4 or length > 100:
        raise HTTPException(
            status_code=400,
            detail="Length must be between 4 and 100"
        )

    if not any([uppercase, lowercase, digits, symbols]):
        raise HTTPException(
            status_code=400,
            detail="Enable at least one character type"
        )

    password = generate_password(
        length,
        uppercase,
        lowercase,
        digits,
        symbols
    )

    return {
        "password": password,
        "length": length
    }
```

---

# Step 13: Interactive API Documentation

FastAPI automatically provides:

### Swagger UI

```
http://127.0.0.1:8000/docs
```

### ReDoc

```
http://127.0.0.1:8000/redoc
```






After completing Day 09, Day 10 could be **QR Code Generator API**.

