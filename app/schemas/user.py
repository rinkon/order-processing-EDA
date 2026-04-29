from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    name: str
    password: str

class UserRead(BaseModel):
    id: int
    email: str
    name: str
    hashed_password: str


class LoginPayload(BaseModel):
    email: str
    password: str
