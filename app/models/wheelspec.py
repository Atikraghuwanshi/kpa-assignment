# app/models/wheelspec.py
from sqlalchemy import Column, Integer, String, Date, JSON
from app.database import Base

class WheelSpec(Base):
    __tablename__ = "wheelspecs"

    id = Column(Integer, primary_key=True, index=True)
    formNumber = Column(String, unique=True, nullable=False)
    submittedBy = Column(String, nullable=False)
    submittedDate = Column(Date, nullable=False)
    fields = Column(JSON, nullable=False)
