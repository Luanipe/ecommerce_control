from typing import List
from fastapi import APIRouter, Depends

from app.core.dependencies import get_auth_user
from app.core.container import Container

from app.models.user_model import User

from app.services.product_service import ProductService
from app.schemas.product_schema import ProductSchema, ProductCreateSchema


router = APIRouter(
    prefix="/products",
    tags=["products"]
)

@router.post("/create", response_model=ProductSchema)
def create_product(
    product_info: ProductCreateSchema,
    service: ProductService = Depends(Container.get_product_service),
    user: User = Depends(get_auth_user)
):
    return service.create_product(product_info, user["id"])


@router.get("/", response_model=List[ProductSchema])
def list_products(service: ProductService = Depends(Container.get_product_service)):
    return service.list_products()


@router.get("/{product_id}", response_model=ProductSchema)
def get_product(product_id: int, service: ProductService = Depends(Container.get_product_service)):
    return service.get_product(product_id)
