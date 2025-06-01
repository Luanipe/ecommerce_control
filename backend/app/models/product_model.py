from typing import List
from sqlalchemy import ForeignKey, String, Float, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import ORMBaseModel


class Product(ORMBaseModel):
    __tablename__ = "products"

    description: Mapped[str] = mapped_column(String, nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    stock_quantity: Mapped[int] = mapped_column(Integer, nullable=False)

    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"), nullable=False)
    category: Mapped["Category"] = relationship(back_populates="products")

    seller_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    seller: Mapped["User"] = relationship(back_populates="products")

    sales: Mapped[List["Sale"]] = relationship(back_populates="product")
