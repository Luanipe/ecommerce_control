from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.dependencies import get_db_session

from app.repositories import *
from app.services import *


class Container:
    # get repositories
    @staticmethod
    def __get_user_repository(db: Session = Depends(get_db_session)) -> UserRepository:
        return UserRepository(db)

    @staticmethod
    def __get_category_repository(db: Session = Depends(get_db_session)) -> CategoryRepository:
        return CategoryRepository(db)

    @staticmethod
    def __get_product_repository(db: Session = Depends(get_db_session)) -> ProductRepository:
        return ProductRepository(db)

    @staticmethod
    def __get_sale_repository(db: Session = Depends(get_db_session)) -> SaleRepository:
        return SaleRepository(db)

    # get services
    @staticmethod
    def get_auth_service(user_repo: UserRepository = Depends(__get_user_repository)) -> AuthService:
        return AuthService(user_repo)

    @staticmethod
    def get_category_service(category_repo: CategoryRepository = Depends(__get_category_repository)) -> CategoryService:
        return CategoryService(category_repo)

    @staticmethod
    def get_product_service(product_repo: ProductRepository = Depends(__get_product_repository)) -> ProductService:
        return ProductService(product_repo)

    @staticmethod
    def get_sale_service(sale_repo: SaleRepository = Depends(__get_sale_repository)) -> SaleService:
        return SaleService(sale_repo)
