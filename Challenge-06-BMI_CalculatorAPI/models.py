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