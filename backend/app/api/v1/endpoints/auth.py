from fastapi import APIRouter, Depends

from app.core.container import Container

from app.services.auth_service import AuthService

from app.schemas.auth_schema import RegisterSchema
from app.schemas.user_schema import UserSchema


router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.post("/register", response_model=UserSchema)
def register(user_info: RegisterSchema, service: AuthService = Depends(Container.get_auth_service)):
    return service.register(user_info)
