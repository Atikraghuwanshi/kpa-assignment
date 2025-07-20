from fastapi import FastAPI
from app.database import engine, Base
from app.routers import pizza, wheelspec

app = FastAPI(title="KPA Assignment API")

Base.metadata.create_all(bind=engine)

app.include_router(pizza.router)
app.include_router(wheelspec.router)

@app.get("/")
def root():
    return {"message": "KPA Assignment API is running"}
