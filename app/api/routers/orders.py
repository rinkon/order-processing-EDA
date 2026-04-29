from fastapi import APIRouter, Depends
from app.api.deps import get_current_user

router = APIRouter()

@router.get("/all")
def get_all_orders(current_user = Depends(get_current_user)):
    user_id = current_user.get("user_id")
    return "This is an authenticated response"