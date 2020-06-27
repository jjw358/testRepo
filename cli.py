from __future__ import print_function

import click

@click.command()
def cli():
    click.echo("Hello, World!")

if __name__ == '__main__':
    cli()
