"""Mosyle Account Operation Enumerations"""
from enum import Enum


class AccountOperation(str, Enum):
    """Mosyle Account Operation Enumerations"""

    LIST = None
    REQUEST = "request"

    def __str__(self) -> str:
        return str.__str__(self)
