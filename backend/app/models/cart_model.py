from typing import List
from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import ORMBaseModel


class Cart(ORMBaseModel):
    __tablename__ = "carts"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), unique=True)
    user: Mapped["User"] = relationship(back_populates="cart")

    items: Mapped[List["CartItem"]] = relationship(back_populates="cart", cascade="all, delete")


class CartItem(ORMBaseModel):
    __tablename__ = "cart_items"

    quantity: Mapped[int] = mapped_column(Integer, nullable=False)

    cart_id: Mapped[int] = mapped_column(ForeignKey("carts.id"))
    cart: Mapped["Cart"] = relationship(back_populates="items")

    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    product: Mapped["Product"] = relationship()

