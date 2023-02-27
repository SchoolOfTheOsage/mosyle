"""Mosyle Manager Python API - API - User Operation"""
from ..str_enum import StrEnum


class UserOperation(StrEnum):
    """Mosyle User Operation Enumerations"""

    SAVE = "save"
    DELETE = "delete"
    ASSIGN_DEVICE = "assign_device"
