from fastapi.security import OAuth2PasswordRequestForm

from middlewares.auth import AuthMiddleware
from app.core.exceptions import DuplicatedError, AuthenticationError

from app.services.base_service import BaseService
from app.repositories.user_repository import UserRepository

from app.schemas.user_schema import UserSchema
from app.schemas.auth_schema import RegisterSchema, TokenSchema


class AuthService(BaseService):
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository
        self.auth = AuthMiddleware()
        super().__init__(user_repository)

    def register(self, user_info: RegisterSchema) -> UserSchema:
        user = self.user_repository.get_by_filter(username=user_info.username)
        
        if user:
            raise DuplicatedError(detail=f"user '{user_info.username}' already exists")
        
        user = RegisterSchema(**user_info.dict())
        user.password = self.auth.encrypt_password(user_info.password)
        created_user = self.user_repository.create(user)
        delattr(created_user, "password")

        return UserSchema.from_orm(created_user)

    def login(self, user_info: OAuth2PasswordRequestForm) -> TokenSchema:
        user = self.user_repository.get_one_by_filter(username=user_info.username)
        
        if not user or not self.auth.verify_password(user_info.password, user.password):
            raise AuthenticationError(detail="invalid username or password")
        
        token = self.auth.create_access_token(data={"sub": user.username})
        return TokenSchema(access_token=token, token_type="bearer")
