from typing import Any

from app.models.user import User
from middlewares.auth import AuthMiddleware
from app.services.base_service import BaseService
from app.repositories.user_repository import UserRepository

from app.schemas.user_schema import UserSchema
from app.schemas.auth_schema import RegisterSchema


class AuthService(BaseService):
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository
        super().__init__(user_repository)

    def register(self, user_info: RegisterSchema) -> UserSchema:
        auth = AuthMiddleware()
        user = User(**user_info.dict(exclude_none=True))
        user.password = auth.encrypt_password(user_info.password)
        created_user = self.user_repository.create(user)
        delattr(created_user, "password")
        # TODO: retornar access token
        return UserSchema.from_orm(created_user)
