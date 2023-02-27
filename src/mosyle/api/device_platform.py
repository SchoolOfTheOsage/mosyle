"""Mosyle Manager Python API - API - Device Platform"""
from ..str_enum import StrEnum


class DevicePlatform(StrEnum):
    """Mosyle Device Platform Enumerations"""

    IOS = "ios"
    MACOS = "macos"
    TVOS = "tvos"
