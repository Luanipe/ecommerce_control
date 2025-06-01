from typing import List

from app.core.exceptions import DuplicatedError

from app.services.base_service import BaseService
from app.repositories.category_repository import CategoryRepository

from app.schemas.category_schema import CategoryCreateSchema, CategorySchema


class CategoryService(BaseService):
    def __init__(self, category_repository: CategoryRepository) -> None:
        self.category_repository = category_repository
        super().__init__(category_repository)

    def create_category(self, category_info: CategoryCreateSchema) -> CategorySchema:
        category = self.category_repository.get_one_by_filter(name=category_info.name)
        if category:
            raise DuplicatedError(detail=f"the category '{category_info.name}' already exists'")
        category = self.category_repository.create(category_info)
        return category

    def list_categories(self) -> List[CategorySchema]:
        return self.category_repository.get_all()
