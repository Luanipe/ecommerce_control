from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base_model import ORMBaseModel


class User(ORMBaseModel):
    __tablename__ = "users"

    username: Mapped[int] = mapped_column(String, nullable=False, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False, index=True)
    last_name: Mapped[str] = mapped_column(String, nullable=False, index=True)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
