from datetime import datetime
from pydantic import Field

from app.schemas.base_schema import BaseSchema, AutoConfigSchema


class SaleBaseSchema(AutoConfigSchema):
    product_id: int
    buyer_id: int
    seller_id: int
    quantity: int = Field(..., gt=0)
    sale_price: float = Field(..., gt=0)
    timestamp: datetime


class SaleCreateSchema(SaleBaseSchema):
    pass


class SaleSchema(BaseSchema, SaleBaseSchema):
    buyer_name: str
    seller_name: str
