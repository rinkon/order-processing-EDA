from fastapi import HTTPException
from app.schemas.user import UserCreate, LoginPayload
from app.models.user import User
from sqlalchemy.orm import Session
from app.core import hashing
from app.core.security import create_token


def register(new_user: UserCreate, db: Session):
    db_user = db.query(User).filter(User.email==new_user.email).first()

    if db_user:
        raise HTTPException(status_code=409, detail="User already exists")

    hashed_password = hashing.hash_password(new_user.password)
    db_user = User(
        **new_user.model_dump(exclude={"password"}),
        hashed_password=hashed_password
    )

    db.add(db_user)
    db.commit()

    return {"message":"Registration successful"}

def login(payload: LoginPayload, db: Session):
    db_user = db.query(User).filter(User.email == payload.email).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="Invalid Credentials")
    
    verified = hashing.verify_hash(hashed=db_user.hashed_password, password=payload.password)

    if not verified:
        raise HTTPException(status_code=404, detail="Invalid Credentials")
    
    token = create_token({
        "sub": str(db_user.id)
    })

    return {
        "access_token": token,
        "type": "bearer"
    }


    