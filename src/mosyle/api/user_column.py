"""Mosyle Manager Python API - API - User Column"""
from ..str_enum import StrEnum


class UserColumn(StrEnum):
    """Mosyle User Column Enumerations"""

    ID = "id"
    NAME = "name"
    EMAIL = "email"
    MANAGED_APPLE_ID = "managedappleid"
    SERIAL_NUMBER = "serial_number"
    TYPE = "type"
    LOCATIONS = "locations"
    ACCOUNT = "account"
