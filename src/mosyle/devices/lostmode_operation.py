from ..str_enum import StrEnum


class LostModeOperation(StrEnum):
    """Device Lost Mode Operation Enumeration"""

    ENABLE = "enable"
    DISABLE = "disable"
    PLAY_SOUND = "play_sound"
    REQUEST_LOCATION = "request_location"
