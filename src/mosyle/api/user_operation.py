"""Mosyle User Operation Enumerations"""
from ..str_enum import StrEnum


class UserOperation(StrEnum):
    """Mosyle User Operation Enumerations"""

    SAVE = "save"
    DELETE = "delete"
    ASSIGN_DEVICE = "assign_device"
