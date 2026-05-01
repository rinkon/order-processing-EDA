from sqlalchemy import Column, Integer, JSON, Enum, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database.base import Base
from sqlalchemy.sql import func
from app.schemas.order import OrderStatus

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True,index=True, autoincrement=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    item_id = Column(Integer, nullable=False)
    quantity = Column(Integer, default=0)
    order_status = Column(Enum(OrderStatus), nullable=False, default=OrderStatus.PENDING)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="orders")





