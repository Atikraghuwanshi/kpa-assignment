from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.pizza import PizzaCreate, PizzaResponse
from app.database import get_db
from app.crud import pizza

router = APIRouter(prefix="/v1/pizzas", tags=["Pizzas"])

@router.post("/", response_model=PizzaResponse)
def create_pizza(data: PizzaCreate, db: Session = Depends(get_db)):
    return pizza.create_pizza(db, data)

@router.get("/", response_model=list[PizzaResponse])
def read_pizzas(db: Session = Depends(get_db)):
    return pizza.get_all_pizzas(db)
