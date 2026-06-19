# 🚀 Challenge 06 - BMI Calculator API 
---

# Project Goal

Build a BMI Calculator API that can:

✅ Calculate BMI from weight and height
✅ Categorize BMI (Underweight, Normal, Overweight, Obese)
✅ Save calculations to a database
✅ Retrieve all BMI records
✅ Retrieve one record by ID
✅ Delete a record

---

# Step 1: Create Project Structure

```
bmi_calculator_api/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── crud.py
```

---

# Step 2: Install Packages

```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic
```

Check:

```bash
pip freeze
```

---

# Step 3: Create PostgreSQL Database

Open PostgreSQL:

```sql
CREATE DATABASE bmi_db;
```

Verify:

```sql
\l
```

You should see:

```
bmi_db
postgres
template0
template1
```

---

# Step 4: Create Table

```sql
CREATE TABLE bmi_records(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    weight FLOAT NOT NULL,
    height FLOAT NOT NULL,
    bmi FLOAT,
    category VARCHAR(30),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

# Step 5: Database Connection

### database.py

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:password@localhost:5432/bmi_db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
```

---

# Step 6: Create Model

### models.py

```python
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Float, String, DateTime
from datetime import datetime


class Base(DeclarativeBase):
    pass


class BMIRecord(Base):
    __tablename__ = "bmi_records"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    weight: Mapped[float] = mapped_column(Float)
    height: Mapped[float] = mapped_column(Float)
    bmi: Mapped[float] = mapped_column(Float)
    category: Mapped[str] = mapped_column(String(30))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
```

---

# Step 7: Create Pydantic Schemas

### schemas.py

```python
from pydantic import BaseModel


class BMICreate(BaseModel):
    name: str
    weight: float
    height: float


class BMIResponse(BMICreate):
    id: int
    bmi: float
    category: str

    class Config:
        from_attributes = True
```

---

# Step 8: BMI Calculation Function

Formula:

```
BMI = weight / (height²)
```

Example:

```python
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    return round(bmi, 2), category
```

---

# Step 9: Create CRUD Functions

### crud.py

```python
from models import BMIRecord


def create_bmi(db, data, bmi, category):
    record = BMIRecord(
        name=data.name,
        weight=data.weight,
        height=data.height,
        bmi=bmi,
        category=category
    )

    db.add(record)
    db.commit()
    db.refresh(record)

    return record
```

---

# Step 10: Main FastAPI File

### main.py

```python
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from schemas import BMICreate
from crud import create_bmi

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    return round(bmi, 2), category


@app.post("/calculate")
def calculate(data: BMICreate, db: Session = Depends(get_db)):

    bmi, category = calculate_bmi(data.weight, data.height)

    record = create_bmi(db, data, bmi, category)

    return {
        "id": record.id,
        "name": record.name,
        "bmi": bmi,
        "category": category
    }
```

---

# Step 11: Run Server

```bash
uvicorn main:app --reload
```

Swagger:

```
http://127.0.0.1:8000/docs
```

---

# Step 12: Test

Request:

```json
{
  "name": "Savindu",
  "weight": 72,
  "height": 1.75
}
```

Response:

```json
{
  "id": 1,
  "name": "Savindu",
  "bmi": 23.51,
  "category": "Normal"
}
```

---

# Step 13: Add More Endpoints

### Get all records

```python
GET /records
```

### Get by ID

```python
GET /records/{id}
```

### Delete record

```python
DELETE /records/{id}
```

---

# Optional Improvements (Good for Day 6)

### Input Validation

```python
from pydantic import BaseModel, Field

class BMICreate(BaseModel):
    name: str
    weight: float = Field(gt=0)
    height: float = Field(gt=0)
```

---

### Add Health Tips

```python
{
    "bmi": 31.2,
    "category": "Obese",
    "advice": "Regular exercise and balanced diet recommended."
}
```

---

### Save Age and Gender

Database:

```sql
age INT,
gender VARCHAR(10)
```

