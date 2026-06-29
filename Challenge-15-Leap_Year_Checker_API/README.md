
# ❤️ Challenge 15 - Leap Year Checker API
---



## 📌 Project Goal

Create an API that checks whether a given year is a leap year.

Example:

```
Input:
2024

Output:
{
   "year": 2024,
   "is_leap_year": true,
   "message": "2024 is a leap year."
}
```

---

# Project Structure

```
leap-year-api/
│
├── main.py

```

---

# Step 1 - Create Project Folder

```bash
mkdir leap-year-api
cd leap-year-api
```

---

# Step 2 - Create Virtual Environment

Windows

```bash
python -m venv venv
```

Linux / Mac

```bash
python3 -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

---

# Step 3 - Install FastAPI

```bash
pip install fastapi uvicorn
```

Save requirements

```bash
pip freeze > requirements.txt
```

---

# Step 4 - Create `main.py`

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Leap Year Checker API",
    description="Check whether a given year is a leap year.",
    version="1.0.0"
)


class YearInput(BaseModel):
    year: int


def is_leap_year(year: int) -> bool:
    """
    Return True if the year is a leap year.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


@app.get("/")
def home():
    return {
        "message": "Welcome to the Leap Year Checker API!"
    }


@app.post("/check")
def check_leap_year(data: YearInput):

    if data.year <= 0:
        raise HTTPException(
            status_code=400,
            detail="Year must be greater than 0."
        )

    leap = is_leap_year(data.year)

    return {
        "year": data.year,
        "is_leap_year": leap,
        "message": (
            f"{data.year} is a leap year."
            if leap
            else f"{data.year} is not a leap year."
        )
    }
```

---

# Step 5 - Run the API

```bash
uvicorn main:app --reload
```

Output

```
INFO: Uvicorn running on http://127.0.0.1:8000
```

---

# Step 6 - Open Swagger UI

Visit

```
http://127.0.0.1:8000/docs
```

You will see interactive API documentation.

---

# Step 7 - Test the API

## Home

GET

```
/
```

Response

```json
{
  "message": "Welcome to the Leap Year Checker API!"
}
```

---

## Check Leap Year

POST

```
/check
```

Request

```json
{
    "year": 2024
}
```

Response

```json
{
    "year": 2024,
    "is_leap_year": true,
    "message": "2024 is a leap year."
}
```

---

Request

```json
{
    "year": 2023
}
```

Response

```json
{
    "year": 2023,
    "is_leap_year": false,
    "message": "2023 is not a leap year."
}
```

---

Invalid Request

```json
{
    "year": -5
}
```

Response

```json
{
  "detail": "Year must be greater than 0."
}
```

---

# Step 8 - Test with cURL

Leap Year

```bash
curl -X POST "http://127.0.0.1:8000/check" \
-H "Content-Type: application/json" \
-d "{\"year\":2024}"
```

Not Leap Year

```bash
curl -X POST "http://127.0.0.1:8000/check" \
-H "Content-Type: application/json" \
-d "{\"year\":2023}"
```

---

# Step 9 - Test with Postman

**Method**

```
POST
```

URL

```
http://127.0.0.1:8000/check
```

Headers

```
Content-Type: application/json
```

Body

```json
{
    "year": 2000
}
```

