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
    items: list[Item]
    order_status: OrderStatus


class OrderRead(BaseModel):
    id: int
    user_id: int
    items: list[Item]
    order_status: OrderStatus
    created_at: datetime