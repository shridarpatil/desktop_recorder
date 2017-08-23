# -*- coding: utf-8 -*-

"""Console script for desktop_screen_recorder."""

from desktop_screen_recorder import builder
import click


@click.command()
def main(args=None):
    """Console script for desktop_screen_recorder."""
    click.echo("Replace this message by putting your code into "
               "desktop_screen_recorder.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")
    builder()


if __name__ == "__main__":
    main()
