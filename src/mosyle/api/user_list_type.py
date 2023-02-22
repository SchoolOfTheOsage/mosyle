"""Mosyle User List Type Enumerations"""
from ..str_enum import StrEnum


class UserListType(StrEnum):
    """Mosyle User List Type Enumerations"""

    STUDENT = "STUDENT"
    TEACHER = "TEACHER"
    LOCATION_LEADER = "LOCATION_LEADER"
    STAFF = "STAFF"
    ADMIN = "ADMIN"
    ACCOUNT_ADMIN = "ACCOUNT_ADMIN"
    DISTRICT_ADMIN = "DISTRICT_ADMIN"
