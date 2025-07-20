# app/routers/wheelspec.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.wheelspec import WheelSpecCreate, WheelSpecResponse
from app.database import get_db
from app.crud import wheelspec

router = APIRouter(prefix="/api/forms/wheel-specifications", tags=["Wheel Specifications"])

@router.post("/", response_model=WheelSpecResponse, status_code=201)
def create_spec(data: WheelSpecCreate, db: Session = Depends(get_db)):
    return wheelspec.create_wheelspec(db, data)

@router.get("/", response_model=list[WheelSpecResponse])
def get_specs(db: Session = Depends(get_db)):
    return wheelspec.get_wheelspecs(db)
