from fastapi import FastAPI
from app.api.routers import auth
from app.api.routers import orders
from app.database.base import Base
from app.database.db import engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/auth")
app.include_router(orders.router, prefix="/orders")