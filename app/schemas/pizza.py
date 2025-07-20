from pydantic import BaseModel
from datetime import datetime

class PizzaCreate(BaseModel):
    name: str
    description: str
    ingredients: str
    price: float

class PizzaResponse(PizzaCreate):
    pizzaId: int
    createdAt: datetime
    updatedAt: datetime

    class Config:
        from_attributes = True  # Pydantic v2 compatibility
