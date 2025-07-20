# app/schemas/wheelspec.py
from pydantic import BaseModel
from typing import Optional
from datetime import date

class WheelSpecBase(BaseModel):
    formNumber: str
    submittedBy: str
    submittedDate: date
    fields: dict

class WheelSpecCreate(WheelSpecBase):
    pass

class WheelSpecResponse(WheelSpecBase):
    id: int

    class Config:
        from_attributes = True
