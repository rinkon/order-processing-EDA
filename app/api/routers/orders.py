from fastapi import APIRouter, Depends, Header
from app.api.deps import get_current_user
from app.services import orders_services
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.schemas.order import *

router = APIRouter()

@router.get("/all")
def get_all_orders(current_user = Depends(get_current_user)):
    user_id = current_user.get("user_id")
    return "This is an authenticated response"

@router.post("/")
def place_order(payload: OrderCreate, current_user = Depends(get_current_user), db: Session = Depends(get_db), idempotency_key = Header(None)):
    user_id = current_user.get("user_id")
    return orders_services.place_order(user_id=user_id, payload=payload, db=db, idempotency_key=idempotency_key)
