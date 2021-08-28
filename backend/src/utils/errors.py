from typing import Sequence

from fastapi import HTTPException, status
from pymongo.errors import DuplicateKeyError


class UniqueConstraintException(HTTPException):
    def __init__(self, *, error: DuplicateKeyError) -> None:
        self._error = error

        detail = {
            "loc": self._parse_loc_from_from_error(),
            "msg": self._get_error_message(),
            "type": "unique_constraint_error",
        }

        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)

    def _parse_loc_from_from_error(self) -> tuple[str]:
        field_name = list(self._error.details["keyValue"].keys())[0]
        return "body", field_name

    def _get_error_message(self) -> str:
        error_dict_keys = list(self._error.details["keyValue"].keys())
        human_readable_field = error_dict_keys[0].replace("_", " ")
        return f"This {human_readable_field} is already used."
