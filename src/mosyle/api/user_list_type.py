"""Mosyle User List Type Enumerations"""
from enum import Enum


class UserListType(str, Enum):
    """Mosyle User List Type Enumerations"""

    STUDENT = "STUDENT"
    TEACHER = "TEACHER"
    LOCATION_LEADER = "LOCATION_LEADER"
    STAFF = "STAFF"
    ADMIN = "ADMIN"
    ACCOUNT_ADMIN = "ACCOUNT_ADMIN"
    DISTRICT_ADMIN = "DISTRICT_ADMIN"

    def __str__(self) -> str:
        return str.__str__(self)
