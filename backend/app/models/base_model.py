from datetime import datetime
from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base

class ORMBaseModel(Base):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now(), onupdate=datetime.now())
