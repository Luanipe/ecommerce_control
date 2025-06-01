from app.schemas.base_schema import BaseSchema, AutoConfigSchema

class CategoryBaseSchema(AutoConfigSchema):
    name: str


class CategoryCreateSchema(CategoryBaseSchema):
    pass


class CategorySchema(BaseSchema, CategoryBaseSchema):
    pass
