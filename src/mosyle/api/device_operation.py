"""Mosyle Device Operation Enumerations"""
from ..str_enum import StrEnum


class DeviceOperation(StrEnum):
    """Mosyle Device Operation Enumerations"""

    WIPE_DEVICES = "wipe_devices"
    RESTART_DEVICES = "restart_devices"
    SHUTDOWN_DEVICES = "shutdown_devices"
    CLEAR_COMMANDS = "clear_commands"
    CLEAR_PENDING_COMMANDS = "clear_pending_commands"
    CLEAR_FAILED_COMMANDS = "clear_failed_commands"
    CHANGE_TO_LIMBO = "change_to_limbo"
