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