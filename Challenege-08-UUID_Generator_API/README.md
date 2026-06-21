# ❤️ Challenge 08 - UUID Generator
---
# 📌 What You'll Learn

* Creating GET endpoints with FastAPI
* Using Python's built-in `uuid` module
* Returning JSON responses
* Generating UUID4 identifiers
* Adding optional count parameters

---

# Step 1: Create Project Folder

```bash
mkdir challenge08_uuid_generator_api
cd challenge08_uuid_generator_api
```

---

# Step 2: Create Virtual Environment

```bash
python -m venv venv
```

Activate it:

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

---

# Step 3: Install FastAPI and Uvicorn

```bash
pip install fastapi uvicorn
```

---

# Step 4: Create `main.py`

```python
from fastapi import FastAPI
import uuid

app = FastAPI(
    title="UUID Generator API",
    description="Generate random UUIDs",
    version="1.0.0"
)
```

---

# Step 5: Create Root Endpoint

```python
@app.get("/")
def home():
    return {
        "message": "Welcome to UUID Generator API"
    }
```

---

# Step 6: Generate One UUID

```python
@app.get("/uuid")
def generate_uuid():
    return {
        "uuid": str(uuid.uuid4())
    }
```

Example response:

```json
{
  "uuid": "1a14dbb3-4fa1-4e14-8d7e-0b0d89ebf8c5"
}
```

---

# Step 7: Generate Multiple UUIDs

```python
@app.get("/uuids/{count}")
def generate_multiple_uuids(count: int):
    ids = [str(uuid.uuid4()) for _ in range(count)]

    return {
        "count": count,
        "uuids": ids
    }
```

Example:

```
GET /uuids/3
```

Response:

```json
{
  "count": 3,
  "uuids": [
    "d3878aeb-4b62-4ef6-a6db-f8bc68db2a75",
    "c9648cc3-d4e2-4d52-b803-9b7f27f2c60f",
    "b8f08983-bcb7-4c17-b5a4-9f9a06dfe214"
  ]
}
```

---

# Step 8: Add UUID Versions Support

```python
@app.get("/uuid/{version}")
def generate_uuid_by_version(version: int):

    if version == 1:
        generated_uuid = uuid.uuid1()

    elif version == 4:
        generated_uuid = uuid.uuid4()

    else:
        return {
            "error": "Only UUID version 1 and 4 are supported"
        }

    return {
        "version": version,
        "uuid": str(generated_uuid)
    }
```

Examples:

```
GET /uuid/1
GET /uuid/4
```

---

# Step 9: Run the API

```bash
uvicorn main:app --reload
```

Output:

```
INFO: Uvicorn running on http://127.0.0.1:8000
```

---

# Step 10: Test Endpoints

### Home

```
GET /
```

### Single UUID

```
GET /uuid
```

### Multiple UUIDs

```
GET /uuids/5
```

### Version Specific UUID

```
GET /uuid/1
```

or

```
GET /uuid/4
```

---

# Complete `main.py`

```python
from fastapi import FastAPI
import uuid

app = FastAPI(
    title="UUID Generator API",
    description="Generate random UUIDs",
    version="1.0.0"
)


@app.get("/")
def home():
    return {"message": "Welcome to UUID Generator API"}


@app.get("/uuid")
def generate_uuid():
    return {
        "uuid": str(uuid.uuid4())
    }


@app.get("/uuids/{count}")
def generate_multiple_uuids(count: int):
    ids = [str(uuid.uuid4()) for _ in range(count)]

    return {
        "count": count,
        "uuids": ids
    }


@app.get("/uuid/{version}")
def generate_uuid_by_version(version: int):

    if version == 1:
        generated_uuid = uuid.uuid1()

    elif version == 4:
        generated_uuid = uuid.uuid4()

    else:
        return {
            "error": "Only UUID version 1 and 4 are supported"
        }

    return {
        "version": version,
        "uuid": str(generated_uuid)
    }
```




