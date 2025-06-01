from sqlalchemy.orm import Session

from app.models.cart_model import CartItem
from app.repositories.base_repository import BaseRepository


class CartItemRepository(BaseRepository):
    def __init__(self, db: Session) -> None:
        self.db = db
        super().__init__(db, CartItem)
