from app.core.exceptions import DuplicatedError
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
        user = self.user_repository.get_by_filter(username=user_info.username)
        if user:
            raise DuplicatedError(detail=f"user '{user_info.username}' already exists")
        auth = AuthMiddleware()
        user = RegisterSchema(**user_info.dict())
        user.password = auth.encrypt_password(user_info.password)
        created_user = self.user_repository.create(user)
        delattr(created_user, "password")
        return UserSchema.from_orm(created_user)
