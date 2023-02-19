from enum import Enum


class ClassPlatform(str, Enum):
    """Class Platforms"""

    IOS = "ios"
    MACOS = "mac"

    def __str__(self) -> str:
        return str.__str__(self)
