"""Mosyle Device Platform Enumerations"""
from enum import Enum


class DevicePlatform(str, Enum):
    """Mosyle Device Platform Enumerations"""

    IOS = "ios"
    MACOS = "macos"
    TVOS = "tvos"

    def __str__(self) -> str:
        return str.__str__(self)
