from typing import Any, Protocol


class RepositoryProtocol(Protocol):
    def get_by_id(self, id: int) -> Any: ...

    def create(self, schema: Any) -> Any: ...

    def update(self, id: int, schema: Any) -> Any: ...

    def update_attribute(self, id: int, column: str, value: Any) -> Any: ...

    def delete_by_id(self, id: int) -> Any: ...


class BaseService:
    def __init__(self, repository: RepositoryProtocol) -> None:
        self.__repository = repository

    def get_by_id(self, id: int) -> Any:
        return self.__repository.get_by_id(id)

    def add(self, schema: Any) -> Any:
        return self.__repository.create(schema)

    def patch(self, id: int, schema: Any) -> Any:
        return self.__repository.update(id, schema)

    def patch_attr(self, id: int, attr: str, value: Any) -> Any:
        return self.__repository.update_attribute(id, attr, value)

    def remove_by_id(self, id: int) -> Any:
        return self.__repository.delete_by_id(id)
