from pydantic import BaseModel

from app.schemas.base_schema import BaseSchema


class UserSchema(BaseSchema):
    username: str
    email: str
    password: str
    name: str
    last_name: str

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str
