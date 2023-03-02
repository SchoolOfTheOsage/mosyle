"""Mosyle Manager Python API - Main"""

import click

import mosyle

from .account import AccountCli
from .action import ActionCli
from .cisco_ise import CiscoIseCli
from .click_order_commands import OrderCommands
from .config import ConfigCli
from .device import DeviceCli
from .section import SectionCli
from .user import UserCli


@click.group(cls=OrderCommands)
@click.version_option(mosyle.__version__)
def main():
    """Mosyle Manager Python API"""


main.add_command(ConfigCli.config)
main.add_command(AccountCli.account)
main.add_command(ActionCli.action)
main.add_command(CiscoIseCli.ciscoise)
main.add_command(DeviceCli.device)
main.add_command(SectionCli.section)
main.add_command(UserCli.user)


if __name__ == "__main__":
    main()
