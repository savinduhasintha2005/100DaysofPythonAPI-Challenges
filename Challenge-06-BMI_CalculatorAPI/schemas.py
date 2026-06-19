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