import jwt
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from config import settings
from auth.repository import UserRepository


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def create_jwt_token(data: dict):
    return jwt.encode(data, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

def get_username_from_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])  # декодируем токен
        return payload.get("sub")
    except jwt.ExpiredSignatureError:
        pass  # тут какая-то логика ошибки истечения срока действия токена
    except jwt.InvalidTokenError:
        pass  # тут какая-то логика обработки ошибки декодирования токена