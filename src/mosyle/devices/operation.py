from ..str_enum import StrEnum


class Operation(StrEnum):
    """Device Operation Enumeration"""

    WIPE = "wipe_devices"
    RESTART = "restart_devices"
    SHUTDOWN = "shutdown_devices"
    CLEAR_COMMANDS = "clear_commands"
    CLEAR_PENDING_COMMANDS = "clear_pending_commands"
    CLEAR_FAILED_COMMANDS = "clear_failed_commands"
    UNASSIGN = "change_to_limbo"
