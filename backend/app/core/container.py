from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.dependencies import get_db_session

from app.repositories import *
from app.services import *


class Container:
    # get repositories
    @staticmethod
    def get_user_repository(db: Session = Depends(get_db_session)):
        return UserRepository(db)

    # get services
    @staticmethod
    def get_auth_service(user_repo: UserRepository = Depends(get_user_repository)):
        return AuthService(user_repo)
