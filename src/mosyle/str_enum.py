"""Mosyle Manager Python API - String Enumeration"""
from enum import Enum


class StrEnum(str, Enum):
    """String Enumeration"""

    def __str__(self) -> str:
        """String Duck Type"""
        return str.__str__(self)
