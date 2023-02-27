"""Mosyle Manager Python API - API - Cisco Ise Operation"""
from ..str_enum import StrEnum


class CiscoIseOperation(StrEnum):
    """Mosyle Cisco Ise Operation Enumerations"""

    ADD = "add"
    REMOVE = "remove"
