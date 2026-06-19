from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from models import BMIRecord
from schemas import BMICreate

from curd import create_bmi, get_all_records

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

@app.get("/records")
def get_records(db: Session = Depends(get_db)):
    return get_all_records(db)

@app.get("/records/{id}")
def get_record(id: int,
               db: Session = Depends(get_db)):

    return db.query(BMIRecord).filter(
        BMIRecord.id == id
    ).first()

@app.delete("/records/{id}")
def delete_record(id: int,
                  db: Session = Depends(get_db)):

    record = db.query(BMIRecord).filter(
        BMIRecord.id == id
    ).first()

    db.delete(record)
    db.commit()

    return {"message": "Deleted"}