from datetime import datetime
from pydantic import EmailStr

from app.schemas.base_schema import AutoConfigSchema
from app.models.user_model import User


class RegisterSchema(AutoConfigSchema):
    username: str
    name: str
    last_name: str
    email: EmailStr
    password: str


class LoginSchema(AutoConfigSchema):
    email__eq: EmailStr
    password: str


class LoginResponseSchema(AutoConfigSchema):
    access_token: str
    expiration: datetime
    user_info: User


class TokenSchema(AutoConfigSchema):
    access_token: str
    token_type: str
