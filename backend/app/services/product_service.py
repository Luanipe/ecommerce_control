from app.services.base_service import BaseService
from app.repositories.product_repository import ProductRepository


class ProductService(BaseService):
    def __init__(self, product_repository: ProductRepository) -> None:
        self.product_repository = product_repository
        super().__init__(product_repository)
