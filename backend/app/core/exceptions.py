from fastapi import HTTPException, status
from typing import Any, Optional, Dict


class NotFoundError(HTTPException):
    def __init__(self, detail: Any = None, headers: Optional[Dict[str, Any]] = None) -> None:
        super().__init__(status.HTTP_404_NOT_FOUND, detail, headers)


class DuplicatedError(HTTPException):
    def __init__(self, detail: Any = None, headers: Optional[Dict[str, Any]] = None) -> None:
        super().__init__(status.HTTP_400_BAD_REQUEST, detail, headers)
