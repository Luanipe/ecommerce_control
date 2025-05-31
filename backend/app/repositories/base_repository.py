from enum import Enum
from typing import Any, TypeVar, Type

from sqlalchemy import asc, desc
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.models.base_model import ORMBaseModel
from app.core.exceptions import NotFoundError, DuplicatedError


T = TypeVar("T")

class Ordering(str, Enum):
    ASC: str = "1"
    DESC: str = "-1"


class BaseRepository:
    def __init__(self,  db: Session, model: Type[T]) -> None:
        self.db = db
        self.model = model

    def get_by_filter(self, ordering: Ordering = Ordering.ASC, order_by_field: str = "id", **kwargs) -> list[dict]:
        query = self.db.query(self.model)

        for field, value in kwargs.items():
            if hasattr(self.model, field):
                query = query.filter(getattr(self.model, field) == value)

        if hasattr(self.model, order_by_field):
            order_column = getattr(self.model, order_by_field)
            if ordering == Ordering.DESC:
                query = query.order_by(desc(order_column))
            else:
                query = query.order_by(asc(order_column))

        results = query.all()
        return [item.__dict__ for item in results]

    def get_by_id(self, id: int) -> Any:
        query = self.db.query(self.model).filter(self.model.id == id).first()
        if not query:
            return NotFoundError(detail=f"id {id} not found")
        return query

    def create(self, schema: T) -> Any:
        query = self.model(**schema.dict())
        try:
            self.db.add(query)
            self.db.commit()
            self.db.refresh(query)
        except IntegrityError as err:
            raise DuplicatedError(detail=str(err.orig))
        return query

    def update(self, id: int, schema: T) -> Any:
        self.db.query(self.model).filter(self.model.id == id).update(schema.dict())
        self.db.commit()
        return self.get_by_id(id)

    def update_attribute(self, id: int, column: str, value: Any) -> Any:
        self.db.query(self.model).filter(self.model.id == id).update({column: value})
        self.db.commit()
        return self.get_by_id(id)

    def delete_by_id(self, id: int) -> None:
        query = self.db.query(self.model).filter(self.model.id == id).first()
        if not query:
            raise NotFoundError(detail=f"id {id} not found")
        self.db.delete(query)
        self.db.commit()
