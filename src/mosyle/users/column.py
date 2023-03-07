from ..str_enum import StrEnum


class Column(StrEnum):
    """User Column Enumeration"""

    ID = "id"
    NAME = "name"
    EMAIL = "email"
    MANAGED_APPLE_ID = "managedappleid"
    SERIAL_NUMBER = "serial_number"
    TYPE = "type"
    LOCATIONS = "locations"
    ACCOUNT = "account"
