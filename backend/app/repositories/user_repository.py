from sqlalchemy.orm import Session

from app.repositories.base_repository import BaseRepository
from app.models.user_model import User


class UserRepository(BaseRepository):
    def __init__(self, db: Session) -> None:
        self.db = db
        super().__init__(db, User)
