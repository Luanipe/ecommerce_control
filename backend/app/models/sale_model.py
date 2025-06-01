from sqlalchemy import ForeignKey, Integer, Float, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import ORMBaseModel


class Sale(ORMBaseModel):
    __tablename__ = "sales"

    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    sale_price: Mapped[float] = mapped_column(Float, nullable=False)
    timestamp: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    product: Mapped["Product"] = relationship(back_populates="sales")

    buyer_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    buyer: Mapped["User"] = relationship(back_populates="purchases", foreign_keys=[buyer_id])

    seller_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    seller: Mapped["User"] = relationship(back_populates="sales_made", foreign_keys=[seller_id])
