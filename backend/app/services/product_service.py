from typing import List

from app.core.exceptions import DuplicatedError

from app.models.product_model import Product
from app.services.base_service import BaseService

from app.repositories.product_repository import ProductRepository

from app.schemas.product_schema import ProductSchema, ProductCreateSchema, UserProductCreateSchema


class ProductService(BaseService):
    def __init__(self, product_repository: ProductRepository) -> None:
        self.product_repository = product_repository
        super().__init__(product_repository)

    def __inject_seller(self, p: Product) -> ProductSchema:
        product_dict = p.__dict__
        product_dict.update({
            "seller_id": p.seller_id,
            "seller_name": p.seller.__str__()
        })
        return ProductSchema(**product_dict)

    def create_product(self, product_info: ProductCreateSchema, seller_id: int) -> ProductSchema:
        product = self.product_repository.get_by_filter(description=product_info.description)
        if product:
            raise DuplicatedError(detail="this product already exists")
        new_product = UserProductCreateSchema(**product_info.dict(), seller_id=seller_id)
        self.product_repository.create_product(new_product)
        product = self.product_repository.get_one_by_filter(description=product_info.description)
        return self.__inject_seller(product)

    def get_product(self, product_id: int) -> ProductSchema:
        return self.__inject_seller(self.product_repository.get_product_by_id(product_id))

    def list_products(self) -> List[ProductSchema]:
        products = [self.__inject_seller(product) for product in self.product_repository.get_all_products()]
        return products
