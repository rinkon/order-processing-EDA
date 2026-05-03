from fastapi import FastAPI
from app.api.routers import auth
from app.api.routers import orders

app = FastAPI()

app.include_router(auth.router, prefix="/auth")
app.include_router(orders.router, prefix="/orders")

