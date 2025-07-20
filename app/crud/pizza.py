from sqlalchemy.orm import Session
from app.models.pizza import Pizza
from app.schemas.pizza import PizzaCreate

def create_pizza(db: Session, pizza_data: PizzaCreate):
    new_pizza = Pizza(**pizza_data.dict())
    db.add(new_pizza)
    db.commit()
    db.refresh(new_pizza)
    return new_pizza

def get_all_pizzas(db: Session):
    return db.query(Pizza).all()
