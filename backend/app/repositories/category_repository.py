from sqlalchemy.orm import Session

from app.models.category_model import Category
from app.repositories.base_repository import BaseRepository


class CategoryRepository(BaseRepository):
    def __init__(self, db: Session):
        self.db = db
        super().__init__(db, Category)
