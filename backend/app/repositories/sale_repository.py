from sqlalchemy.orm import Session

from app.models.sale_model import Sale

from app.repositories.base_repository import BaseRepository
from app.repositories.user_repository import UserRepository
from app.repositories.product_repository import ProductRepository


class SaleRepository(BaseRepository):
    def __init__(self, db: Session) -> None:
        self.db = db
        self.user_repository = UserRepository(db)
        self.product_repository = ProductRepository(db)
        super().__init__(db, Sale)
