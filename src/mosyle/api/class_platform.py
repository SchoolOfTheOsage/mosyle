"""Mosyle Class Platform Enumerations"""
from enum import Enum


class ClassPlatform(str, Enum):
    """Mosyle Class Platform Enumerations"""

    IOS = "ios"
    MACOS = "mac"

    def __str__(self) -> str:
        return str.__str__(self)
