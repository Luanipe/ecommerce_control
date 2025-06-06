from pydantic import Field
from app.schemas.base_schema import AutoConfigSchema, BaseSchema


class ProductBaseSchema(AutoConfigSchema):
    description: str
    price: float = Field(..., gt=0)
    stock_quantity: int = Field(..., ge=0)
    category_id: int


class ProductCreateSchema(ProductBaseSchema):
    pass


class UserProductCreateSchema(ProductBaseSchema):
    seller_id: int


class ProductSchema(BaseSchema, ProductBaseSchema):
    seller_id: int
    seller_name: str
