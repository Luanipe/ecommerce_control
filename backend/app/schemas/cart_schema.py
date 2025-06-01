from typing import List
from pydantic import Field

from app.schemas.base_schema import BaseSchema, AutoConfigSchema


class CartItemBaseSchema(AutoConfigSchema):
    product_id: int
    quantity: int = Field(..., gt=0)


class CartItemCreateSchema(CartItemBaseSchema):
    pass


class CartItemSchema(BaseSchema, CartItemBaseSchema):
    pass


class CartSchema(BaseSchema):
    user_id: int
    items: List[CartItemSchema]
