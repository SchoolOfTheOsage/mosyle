"""Mosyle User Operation Type Enumerations"""
from enum import Enum


class UserOperationType(str, Enum):
    """Mosyle User Operation Type Enumerations"""

    STUDENT = "S"
    TEACHER = "T"
    STAFF = "STAFF"

    def __str__(self) -> str:
        return str.__str__(self)
