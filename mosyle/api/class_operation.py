"""Mosyle Class Operation Enumerations"""
from enum import Enum


class ClassOperation(str, Enum):
    """Mosyle Class Operation Enumerations"""

    SAVE = "save"
    DELETE = "delete"

    def __str__(self) -> str:
        return str.__str__(self)
