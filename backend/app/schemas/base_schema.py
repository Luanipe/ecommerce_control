from datetime import datetime
from pydantic import BaseModel


class AutoConfigSchema(BaseModel):
    model_config = {
        "arbitrary_types_allowed": True
    }


class BaseSchema(AutoConfigSchema):
    id: int
    created_at: datetime
    updated_at: datetime
