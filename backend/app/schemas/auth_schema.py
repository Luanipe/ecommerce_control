from pydantic import EmailStr

from app.schemas.base_schema import AutoConfigSchema


class RegisterSchema(AutoConfigSchema):
    username: str
    name: str
    last_name: str
    email: EmailStr
    password: str


class TokenSchema(AutoConfigSchema):
    access_token: str
    token_type: str
