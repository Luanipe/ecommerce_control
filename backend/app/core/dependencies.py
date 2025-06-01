from functools import lru_cache

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from typing_extensions import Annotated, Generator
from sqlalchemy.orm import Session

from config import Settings
from app.core.exceptions import AuthenticationError, NotFoundError
from middlewares.auth import AuthMiddleware

from app.core.database import Database
from app.models.user_model import User
from app.repositories.user_repository import UserRepository


oauth2_authenticator = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


@lru_cache()
def get_settings() -> Settings:
    return Settings()


def get_db_session(settings: Annotated[Settings, Depends(get_settings)]) -> Generator[Session, None, None]:
    db_url = settings.get_db_url()
    db = Database(db_url)
    yield from db.get_session()


def get_auth_user(token: str = Depends(oauth2_authenticator), db: Session = Depends(get_db_session)) -> User:
    auth = AuthMiddleware()
    username = auth.decode_access_token(token)
    if username is None:
        raise AuthenticationError(
            detail="invalid or expired token", headers={"WWW-Authenticate": "Bearer"}
        )
    repo = UserRepository(db)
    user = repo.get_one_by_filter(username=username)
    if not user:
        raise NotFoundError(detail=f"user '{username}' not found")
    return user
