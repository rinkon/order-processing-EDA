from app.database.base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__="users"
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    email = Column(String(30), nullable=False)
    name = Column(String(50), nullable=False)
    hashed_password = Column(String(100), nullable=False)
    orders = relationship("Order", back_populates="user")


