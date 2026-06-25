# ❤️ Challenge 11 - Text Case Convertor API
---

# Step 1: Project Folder Create 

```bash
mkdir text-case-converter-api
cd text-case-converter-api
```

---

# Step 2: Virtual Environment Create 

### Windows

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# Step 3: Install Required Packages

```bash
pip install fastapi uvicorn
```

---

# Step 4: Create Project Structure

```text
text-case-converter-api/
│
├── main.py
├── models.py

```

---

# Step 5: Create models.py
.

```python
from pydantic import BaseModel


class TextRequest(BaseModel):
    text: str


class TextResponse(BaseModel):
    original: str
    uppercase: str
    lowercase: str
    titlecase: str
    capitalize: str
```

---

# Step 6: Create main.py

```python
from fastapi import FastAPI
from models import TextRequest, TextResponse

app = FastAPI(
    title="Text Case Converter API",
    description="Convert text into different cases",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to Text Case Converter API"
    }


@app.post("/convert", response_model=TextResponse)
def convert_text(data: TextRequest):

    text = data.text

    return TextResponse(
        original=text,
        uppercase=text.upper(),
        lowercase=text.lower(),
        titlecase=text.title(),
        capitalize=text.capitalize()
    )
```

---

# Step 7: Create requirements.txt

```text
fastapi
uvicorn
pydantic
```

Generate automatically:

```bash
pip freeze > requirements.txt
```

---

# Step 8: Run the API

```bash
uvicorn main:app --reload
```

Output:

```text
INFO: Uvicorn running on http://127.0.0.1:8000
```

---

# Step 9: Open Swagger UI


```text
http://127.0.0.1:8000/docs
```

---

# Step 10: Test API

### Endpoint

```http
POST /convert
```

Request Body:

```json
{
  "text": "hello world from api"
}
```

Click **Execute**

---

# Response

```json
{
  "original": "hello world from api",
  "uppercase": "HELLO WORLD FROM API",
  "lowercase": "hello world from api",
  "titlecase": "Hello World From Api",
  "capitalize": "Hello world from api"
}
```

---

# Step 11: Test More Examples

### Input

```json
{
  "text": "python FASTAPI challenge"
}
```

Response

```json
{
  "original": "python FASTAPI challenge",
  "uppercase": "PYTHON FASTAPI CHALLENGE",
  "lowercase": "python fastapi challenge",
  "titlecase": "Python Fastapi Challenge",
  "capitalize": "Python fastapi challenge"
}
```

---

# Step 12: Add Error Validation (Bonus)

```python
from pydantic import BaseModel, Field

class TextRequest(BaseModel):
    text: str = Field(
        min_length=1,
        max_length=1000,
        description="Enter text to convert"
    )
```


මේක GitHub එකට push කරලා **"Day 11 - Text Case Converter API"** ලෙස API Challenge repository එකට add කරන්න.

