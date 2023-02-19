"""Mosyle Device Lost Mode Operations"""
from enum import Enum


class DeviceLostModeOperation(str, Enum):
    """Mosyle Device Lost Mode Operations"""

    ENABLE = "enable"
    DISABLE = "disable"
    PLAY_SOUND = "play_sound"
    REQUEST_LOCATION = "request_location"

    def __str__(self) -> str:
        return str.__str__(self)
