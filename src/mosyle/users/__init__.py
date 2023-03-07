"""Mosyle Manager Python API - Device"""
from dataclasses import dataclass

from .column import Column
from .list_type import ListType
from .operation import Operation
from .operation_type import OperationType


@dataclass(frozen=True, slots=True)
class User:
    """User"""

    def get(
        self,
        page: int | None = None,
        specific_columns: list[Column] | None = None,
        types: list[ListType] | None = None,
    ):
        """List Users"""

        options: dict[str, object] = {}
        if page is not None:
            options["page"] = page
        if specific_columns is not None:
            options["specific_columns"] = specific_columns
        if types is not None:
            options["types"] = types

        # return self.post(Endpoint.LIST_USERS, options=options)

    def operation(
        self,
        user_id: str,
        operation: Operation,
        name: str | None = None,
        user_type: OperationType | None = None,
        email: str | None = None,
        managed_apple_id: str | None = None,
        locations: list[tuple[str, str]]
        | None = None,  # List of tuples of (location_name, grade_level)
        welcome_email: bool | None = None,
        serial_number: str | None = None,
    ):
        """User Operations"""

        element: dict[str, object] = {
            "id": user_id,
            "operation": operation,
        }
        if name is not None:
            element["name"] = name
        if user_type is not None:
            element["type"] = user_type
        if email is not None:
            element["email"] = email
        if managed_apple_id is not None:
            element["managed_appleid"] = managed_apple_id
        if locations is not None:
            element["locations"] = locations
        if welcome_email is not None:
            element["welcome_email"] = welcome_email
        if serial_number is not None:
            element["serial_number"] = serial_number

        # return self.post(Endpoint.USERS, elements=[element])
