from typing import List

from app.core.exceptions import NotFoundError, UnavailableError

from app.services.base_service import BaseService

from app.models.sale_model import Sale
from app.repositories.sale_repository import SaleRepository

from app.schemas.sale_schema import SaleBaseSchema, SaleSchema, SaleCreateSchema


class SaleService(BaseService):
    def __init__(self, sale_repository: SaleRepository) -> None:
        self.sale_repository = sale_repository
        super().__init__(sale_repository)

    def __inject_users(self, s: Sale) -> SaleSchema:
        sale_dict = s.__dict__
        sale_dict.update({
            "buyer_name": s.buyer.__str__(),
            "seller_name": s.seller.__str__()
        })
        return SaleSchema(**sale_dict)

    def create_sale(self, sale_info: SaleCreateSchema) -> SaleBaseSchema:
        product = self.sale_repository.product_repository.get_product_by_id(sale_info.product_id)
        if not product or product.stock_quantity < sale_info.quantity:
            raise UnavailableError(detail="unavailable stock or product")

        seller = self.sale_repository.user_repository.get_by_id(sale_info.seller_id)
        if not seller:
            raise NotFoundError(detail="seller not found")

        buyer = self.sale_repository.user_repository.get_by_id(sale_info.buyer_id)
        if not buyer:
            raise NotFoundError(detail="buyer not found")

        product.stock_quantity -= sale_info.quantity
        self.sale_repository.product_repository.update_attribute(product.id, column="stock_quantity",
                                                                 value=product.stock_quantity)
        return self.sale_repository.create(sale_info)

    def list_sales(self) -> List[SaleSchema]:
        sales = [self.__inject_users(sale) for sale in self.sale_repository.get_all()]
        return sales
