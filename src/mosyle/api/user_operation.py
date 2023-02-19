"""Mosyle User Operation Enumerations"""
from enum import Enum


class UserOperation(str, Enum):
    """Mosyle User Operation Enumerations"""

    SAVE = "save"
    DELETE = "delete"
    ASSIGN_DEVICE = "assign_device"

    def __str__(self) -> str:
        return str.__str__(self)
