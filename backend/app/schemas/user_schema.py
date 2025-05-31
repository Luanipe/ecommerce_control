from pydantic import BaseModel
from typing import Optional

from app.schemas.base_schema import BaseSchema


class UserSchema(BaseSchema):
    username: str
    email: str
    password: str
    name: str
    last_name: str


class Token(BaseModel):
    access_token: str
    token_type: str
