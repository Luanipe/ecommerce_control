from datetime import datetime, timedelta
from passlib.context import CryptContext
from jose import JWTError, jwt

from config import settings


class AuthMiddleware:
    __SECRET_KEY: str = settings.jwt_secret_key
    __ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

    def __init__(self) -> None:
        self.__pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def encrypt_password(self, password: str) -> str:
        return self.__pwd_context.hash(password)

    def verify_password(self, raw_password: str, hashed_password: str) -> bool:
        return self.__pwd_context.verify(raw_password, hashed_password)

    def create_access_token(self, data: dict, expires_delta: timedelta = None) -> str:
        to_encode = data.copy()
        expire = datetime.utcnow() + (expires_delta or timedelta(minutes=self.ACCESS_TOKEN_EXPIRE_MINUTES))
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, self.__SECRET_KEY, algorithm=self.__ALGORITHM)

    def decode_access_token(self, token: str) -> str | None:
        try:
            payload = jwt.decode(token, self.__SECRET_KEY, algorithms=[self.__ALGORITHM])
            expire = payload.get("exp")
            if expire and datetime.utcfromtimestamp(expire) < datetime.utcnow():
                return None
            return payload.get("sub")
        except JWTError:
            return None
