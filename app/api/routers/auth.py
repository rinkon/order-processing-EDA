from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, LoginPayload
from app.database.db import get_db
from app.services import auth_services

router = APIRouter()

@router.post("/register")
def register(new_user: UserCreate, db: Session = Depends(get_db)):
    return auth_services.register(new_user=new_user, db=db)


@router.post("/login")
def login(payload: LoginPayload, db: Session = Depends(get_db)):
    return auth_services.login(payload=payload)

