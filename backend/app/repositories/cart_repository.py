from typing import Any
from sqlalchemy.orm import Session

from app.models.cart_model import Cart
from app.schemas.cart_schema import CartSchema
from app.repositories.base_repository import BaseRepository


class CartRepository(BaseRepository):
    def __init__(self, db: Session) -> None:
        self.db = db
        super().__init__(db, Cart)

    def get_or_create(self, user_id: int) -> Any:
        cart = self.get_one_by_filter(user_id=user_id)
        if not cart:
            cart = CartSchema(user_id=user_id, items=[])
            self.create(cart)
        return cart
