from ..str_enum import StrEnum


class ListType(StrEnum):
    """User List Type Enumeration"""

    STUDENT = "STUDENT"
    TEACHER = "TEACHER"
    LOCATION_LEADER = "LOCATION_LEADER"
    STAFF = "STAFF"
    ADMIN = "ADMIN"
    ACCOUNT_ADMIN = "ACCOUNT_ADMIN"
    DISTRICT_ADMIN = "DISTRICT_ADMIN"
