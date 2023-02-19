from enum import Enum


class ClassOperation(str, Enum):
    """Class Operations"""

    SAVE = "save"
    DELETE = "delete"

    def __str__(self) -> str:
        return str.__str__(self)
