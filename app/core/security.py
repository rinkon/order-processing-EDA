from jose import jwt
from datetime import datetime, timedelta
from app.core import config

def create_token(data: dict):
    exp = datetime.now() + timedelta(minutes=config.TOKEN_EXPIRY_IN_MINUTES)
    data.update({"exp": exp})
    return jwt.encode(data, config.SECRET_KEY, "HS256")
