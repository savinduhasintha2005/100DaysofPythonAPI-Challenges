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

def get_all_records(db):
    return db.query(BMIRecord).all()