from fastapi import HTTPException
from app.schemas.order import *
from sqlalchemy.orm import Session
from redis import Redis
import json

redis_client = Redis("localhost", port=6379, decode_responses=True)




def place_order(user_id: int, payload: OrderCreate, db: Session, idempotency_key: str):
    # 
    if idempotency_key is None:
        raise HTTPException(status_code=400, detail="Missing Idempotency-Key in header")
    
    if redis_client.exists(idempotency_key):
        value = redis_client.get(idempotency_key)
        return json.loads(value)
    
    response = {"message": "order placed", "order_id": 00}
    redis_client.set(idempotency_key, json.dumps(response))
    
    return response

    
    

    