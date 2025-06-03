from typing import List, Any
from sqlalchemy.orm import Session

from app.core.exceptions import NotFoundError

from app.models.user_model import User
from app.models.product_model import Product

from app.repositories.base_repository import BaseRepository
from app.repositories.category_repository import CategoryRepository

from app.schemas.product_schema import UserProductCreateSchema


class ProductRepository(BaseRepository):
    def __init__(self, db: Session) -> None:
        self.db = db
        self.category_repository = CategoryRepository(self.db)
        super().__init__(db, Product)

    def get_all_products(self, join_model: Any = User.products) -> List[Product]:
        return self.get_all(join_model)

    def get_product_by_id(self, id: int, join_model: Any = User.products) -> Product:
        product = self.get_by_id(id, join_model=join_model)
        if not product:
            raise NotFoundError(detail="product not found")
        return product

    def create_product(self, product_info: UserProductCreateSchema) -> Product:
        if not self.category_repository.get_by_id(product_info.category_id):
            raise NotFoundError(detail="category not found")
        return self.create(product_info)
