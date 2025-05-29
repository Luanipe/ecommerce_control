from fastapi import Depends
from functools import lru_cache
from typing_extensions import Annotated, Generator
from sqlalchemy.orm import Session

from config import Settings
from app.core.database import Database


@lru_cache()
def get_settings() -> Settings:
    return Settings()


def get_db_session(settings: Annotated[Settings, Depends(get_settings)]) -> Generator[Session, None, None]:
    db_url = settings.get_db_url()
    db = Database(db_url)
    yield from db.get_session()
