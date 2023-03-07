"""Mosyle Manager Python API - CLI"""

import click

from . import __version__
from .actions.cli import Cli as ActionsCli
from .classes import classes
from .configuration.cli import Cli as ConfigurationCli
from .devices.cli import Cli as DevicesCli

# from .rosters.cli import Cli as RostersCli
from .users.cli import Cli as UsersCli

# from .locations.cli import Cli as LocationsCli


@click.group()
@click.version_option(__version__)
def mosyle():
    """Mosyle Manager Python API"""


mosyle.add_command(ConfigurationCli.configuration)
# mosyle.add_command(ActionsCli.actions)
mosyle.add_command(classes)
# mosyle.add_command(DevicesCli.devices)
# mosyle.add_command(UsersCli.users)


if __name__ == "__main__":
    mosyle()
