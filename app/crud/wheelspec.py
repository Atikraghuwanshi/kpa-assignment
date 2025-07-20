# app/crud/wheelspec.py
from sqlalchemy.orm import Session
from app.models.wheelspec import WheelSpec
from app.schemas.wheelspec import WheelSpecCreate

def create_wheelspec(db: Session, data: WheelSpecCreate):
    wheelspec = WheelSpec(**data.dict())
    db.add(wheelspec)
    db.commit()
    db.refresh(wheelspec)
    return wheelspec

def get_wheelspecs(db: Session):
    return db.query(WheelSpec).all()
