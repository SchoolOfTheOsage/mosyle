import click


class Cli:
    "User CLI"

    @staticmethod
    @click.group()
    def users():
        """User"""
        click.echo("Not implemented")
