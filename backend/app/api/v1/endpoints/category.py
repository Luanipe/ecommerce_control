from typing import List
from fastapi import APIRouter, Depends

from app.core.dependencies import get_auth_user
from app.core.container import Container

from app.models.user_model import User

from app.services.category_service import CategoryService
from app.schemas.category_schema import CategorySchema, CategoryCreateSchema


router = APIRouter(
    prefix="/categories",
    tags=["categories"]
)


@router.post("/create", response_model=CategorySchema)
def create_category(
    category_info: CategoryCreateSchema,
    service: CategoryService = Depends(Container.get_category_service),
    _: User = Depends(get_auth_user)
):
    return service.create_category(category_info)


@router.get("/", response_model=List[CategorySchema])
def list_categories(service: CategoryService = Depends(Container.get_category_service)):
    return service.list_categories()


