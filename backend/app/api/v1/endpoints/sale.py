from typing import List
from fastapi import APIRouter, Depends

from app.core.dependencies import get_auth_user
from app.core.container import Container

from app.models.user_model import User

from app.services.sale_service import SaleService
from app.schemas.sale_schema import SaleSchema, SaleCreateSchema


router = APIRouter(
    prefix="/sales",
    tags=["sales"]
)


@router.post("/create", response_model=SaleSchema)
def create_sale(
    sale_info: SaleCreateSchema,
    service: SaleService = Depends(Container.get_sale_service),
    _: User = Depends(get_auth_user)
):
    return service.create_sale(sale_info)


@router.get("/", response_model=List[SaleSchema])
def list_sales(service: SaleService = Depends(Container.get_sale_service)):
    return service.list_sales()
