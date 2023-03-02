"""Mosyle Manager Python API - Main"""

import click

import mosyle

from .config import Config

CONFIG = Config()


# Main
@click.group()
@click.version_option(mosyle.__version__)
def cli():
    """Mosyle Manager CLI"""


# Configuration
@cli.command()
@click.option(
    "-t",
    "--token",
    prompt="API Token",
    default=CONFIG.token_obfuscated,
    help="API Token",
)
@click.option(
    "-u",
    "--username",
    prompt="Username",
    default=CONFIG.username,
    help="Admin Email",
)
@click.password_option(
    "-p",
    "--password",
    prompt="Password",
    default=CONFIG.password_obfuscated,
    help="Admin Password",
    hide_input=True,
    confirmation_prompt=False,
)
def config(token: str, username: str, password: str):
    """Configuration Setup"""
    CONFIG.token_obfuscated = token
    CONFIG.username = username
    CONFIG.password_obfuscated = password


# Account
@cli.command()
def account():
    """Manage Accounts"""
    click.echo("Mosyle Manager Accounts")


# Action


@cli.command()
def action():
    """Manage Actions"""
    click.echo("Mosyle Manager Actions")


# Cisco ISE
@cli.command()
def ciscoise():
    """Manage Cisco ISE"""
    click.echo("Mosyle Manager Cisco ISE")


# Device
@cli.command()
def device():
    """Manage Devices"""
    click.echo("Mosyle Manager Devices")


# Section
@cli.command()
def section():
    """Manage Classes"""
    click.echo("Mosyle Manager Classes")


# User
@cli.command()
def user():
    """Manage Users"""
    click.echo("Mosyle Manager Users")


if __name__ == "__main__":
    cli()
