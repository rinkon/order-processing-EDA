from fastapi import HTTPException
from app.schemas.order import *
from sqlalchemy.orm import Session
from redis import Redis
import json
from app.models.order import Order
from app.workers.orders import process_order

redis_client = Redis("localhost", port=6379, decode_responses=True)


def place_order(user_id: int, payload: OrderCreate, db: Session, idempotency_key: str):
    # 
    if idempotency_key is None:
        raise HTTPException(status_code=400, detail="Missing Idempotency-Key in header")
    
    if redis_client.exists(idempotency_key):
        value = redis_client.get(idempotency_key)
        return json.loads(value)
    
    db_order = Order(
        **payload.model_dump(),
        user_id=user_id
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)

    process_order.delay(db_order.id)

    response = {"message": "order placed", "order_id": db_order.id}
    redis_client.set(idempotency_key, json.dumps(response))
    
    return response

    
    
def get_user_orders(user_id: int, db: Session):
    db_orders = db.query(Order).filter(Order.user_id == user_id).all()
    return db_orders
    