"""Mosyle Manager Python API - Main"""

import click

import mosyle

from .config import Config

CONFIG = Config()


# Main
@click.group()
def cli():
    """Mosyle Manager CLI"""
    click.echo(f"Mosyle Manager CLI {mosyle.__version__}")


# Settings
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
@click.option(
    "-p",
    "--password",
    prompt="Password",
    default=CONFIG.password_obfuscated,
    help="Admin Password",
)
def config(token: str, username: str, password: str):
    """Mosyle Manager CLI Configuration"""
    CONFIG.token_obfuscated = token
    CONFIG.username = username
    CONFIG.password_obfuscated = password


# Account

# Action

# Cisco ISE

# Device


# Section

# User
if __name__ == "__main__":
    cli()
