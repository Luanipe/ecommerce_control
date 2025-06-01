from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.core.container import Container

from app.services.auth_service import AuthService

from app.schemas.user_schema import UserSchema
from app.schemas.auth_schema import RegisterSchema, TokenSchema


router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.post("/register", response_model=UserSchema)
def register(user_info: RegisterSchema, service: AuthService = Depends(Container.get_auth_service)):
    return service.register(user_info)


@router.post("/login", response_model=TokenSchema)
def login(user_info: OAuth2PasswordRequestForm = Depends(), service: AuthService = Depends(Container.get_auth_service)):
    return service.login(user_info)
