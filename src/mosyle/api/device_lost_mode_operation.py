"""Mosyle Manager Python API - API - Device Lost Mode Operation"""
from ..str_enum import StrEnum


class DeviceLostModeOperation(StrEnum):
    """Mosyle Device Lost Mode Operations"""

    ENABLE = "enable"
    DISABLE = "disable"
    PLAY_SOUND = "play_sound"
    REQUEST_LOCATION = "request_location"
