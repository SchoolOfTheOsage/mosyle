from enum import Enum


class UserColumn(str, Enum):
    """User Columns"""

    ID = "id"
    NAME = "name"
    EMAIL = "email"
    MANAGED_APPLE_ID = "managedappleid"
    SERIAL_NUMBER = "serial_number"
    TYPE = "type"
    LOCATIONS = "locations"
    ACCOUNT = "account"

    def __str__(self) -> str:
        return str.__str__(self)
