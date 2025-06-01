from sqlalchemy.orm import Session

from app.models.product_model import Product
from app.repositories.base_repository import BaseRepository


class ProductRepository(BaseRepository):
    def __init__(self, db: Session) -> None:
        self.db = db
        super().__init__(db, Product)
