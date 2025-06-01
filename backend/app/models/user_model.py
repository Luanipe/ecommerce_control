from typing import List
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import ORMBaseModel


class User(ORMBaseModel):
    __tablename__ = "users"

    username: Mapped[int] = mapped_column(String, nullable=False, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False, index=True)
    last_name: Mapped[str] = mapped_column(String, nullable=False, index=True)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)

    cart: Mapped["Cart"] = relationship(back_populates="user", uselist=False)
    products: Mapped[List["Product"]] = relationship(back_populates="seller")
    purchases: Mapped[List["Sale"]] = relationship(back_populates="buyer", foreign_keys="[Sale.buyer_id]")
    sales_made: Mapped[List["Sale"]] = relationship(back_populates="seller", foreign_keys="[Sale.seller_id]")

