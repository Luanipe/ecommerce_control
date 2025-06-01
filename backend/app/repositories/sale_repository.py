from sqlalchemy.orm import Session

from app.models.sale_model import Sale
from app.repositories.base_repository import BaseRepository


class SaleRepository(BaseRepository):
    def __init__(self, db: Session) -> None:
        self.db = db
        super().__init__(db, Sale)
