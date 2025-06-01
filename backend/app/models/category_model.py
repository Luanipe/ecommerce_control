from typing import List
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import ORMBaseModel


class Category(ORMBaseModel):
    __tablename__ = "categories"

    name: Mapped[str] = mapped_column(String, nullable=False)

    products: Mapped[List["Product"]] = relationship(back_populates="category")
