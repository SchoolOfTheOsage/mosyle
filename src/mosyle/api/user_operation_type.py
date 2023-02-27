"""Mosyle Manager Python API - API - User Operation Type"""
from ..str_enum import StrEnum


class UserOperationType(StrEnum):
    """Mosyle User Operation Type Enumerations"""

    STUDENT = "S"
    TEACHER = "T"
    STAFF = "STAFF"
