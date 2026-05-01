from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class OrderStatus(str, Enum):
    PENDING = "PENDING"
    PROCESSING = "PROCESSING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"

class Item(BaseModel):
    item_id: int
    quantity: int


class OrderCreate(BaseModel):
    item_id: int
    quantity: int


class OrderRead(BaseModel):
    id: int
    user_id: int
    item_id: int
    quantity: int
    order_status: OrderStatus
    created_at: datetime