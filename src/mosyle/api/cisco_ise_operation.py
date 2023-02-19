"""Mosyle Cisco Ise Operation Enumerations"""
from enum import Enum


class CiscoIseOperation(str, Enum):
    """Mosyle Cisco Ise Operation Enumerations"""

    ADD = "add"
    REMOVE = "remove"

    def __str__(self) -> str:
        return str.__str__(self)
