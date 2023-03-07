from ..str_enum import StrEnum


class Operation(StrEnum):
    """User Operation Enumeration"""

    SAVE = "save"
    DELETE = "delete"
    ASSIGN_DEVICE = "assign_device"
