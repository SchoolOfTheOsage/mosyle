from enum import Enum


class UserOperationType(str, Enum):
    """User Operation Types"""

    STUDENT = "S"
    TEACHER = "T"
    STAFF = "STAFF"

    def __str__(self) -> str:
        return str.__str__(self)
