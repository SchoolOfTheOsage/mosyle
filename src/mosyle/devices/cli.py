import click


class Cli:
    "Device CLI"

    @staticmethod
    @click.group()
    def devices():
        """Device"""
        click.echo("Not implemented")
