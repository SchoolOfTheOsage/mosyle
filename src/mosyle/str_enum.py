"""String Enumeration"""
from enum import Enum


class StrEnum(str, Enum):
    """String Enumeration"""

    def __str__(self) -> str:
        return str.__str__(self)
