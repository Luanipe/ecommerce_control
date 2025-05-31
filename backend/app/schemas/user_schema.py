from app.schemas.base_schema import BaseSchema


class UserSchema(BaseSchema):
    username: str
    email: str
    name: str
    last_name: str
