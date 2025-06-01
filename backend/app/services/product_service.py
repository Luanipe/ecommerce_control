from typing import List

from app.core.exceptions import DuplicatedError

from app.services.base_service import BaseService
from app.repositories.product_repository import ProductRepository

from app.schemas.product_schema import ProductSchema, ProductCreateSchema, UserProductCreateSchema


class ProductService(BaseService):
    def __init__(self, product_repository: ProductRepository) -> None:
        self.product_repository = product_repository
        super().__init__(product_repository)

    def create_product(self, product_info: ProductCreateSchema, seller_id: int) -> ProductSchema:
        product = self.product_repository.get_by_filter(description=product_info.description)
        if product:
            raise DuplicatedError(detail="this product already exists")
        new_product = UserProductCreateSchema(**product_info.dict(), seller_id=seller_id)
        product = self.product_repository.create(new_product)
        return product

    def get_product(self, product_id: int) -> ProductSchema:
        return self.get_by_id(product_id)

    def list_products(self) -> List[ProductSchema]:
        return self.product_repository.get_all()
