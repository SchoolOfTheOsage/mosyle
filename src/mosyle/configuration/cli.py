import click

from .config import Config

CONFIG = Config()


class Cli:
    """Configuration CLI"""

    @click.group()
    @staticmethod
    def configuration():
        """Configuration"""

    @staticmethod
    @configuration.command()
    @click.option(
        "-t",
        "--token",
        prompt="API Token",
        default=CONFIG.token_obfuscated,
        help="API Token",
    )
    def token(token: str):
        """Access Token"""
        CONFIG.token_obfuscated = token

    @staticmethod
    @configuration.command()
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
    def authorization(username: str, password: str):
        """Username/Password - Required for API calls where an action is generated."""
        CONFIG.username = username
        CONFIG.password_obfuscated = password
