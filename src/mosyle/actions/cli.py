import click


class Cli:
    "Action CLI"

    @staticmethod
    @click.group()
    def actions():
        """Action"""
        click.echo("Not implemented")
