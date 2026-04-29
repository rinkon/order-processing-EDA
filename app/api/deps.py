from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
from app.core import config

security = HTTPBearer()


def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials

    try:
        payload = jwt.decode(token, config.SECRET_KEY, ["HS256"])
        if payload is None:
            raise HTTPException(status_code=401, detail="Invalid token")

        user_id = payload.get("sub")

        return {
            "user_id": int(user_id)
        }

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
