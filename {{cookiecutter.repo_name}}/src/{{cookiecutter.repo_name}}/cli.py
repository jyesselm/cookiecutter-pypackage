"""Command-line interface for {{ cookiecutter.project_name }}."""

import click


@click.group()
def cli() -> None:
    """{{ cookiecutter.project_short_description }}"""
    pass


@cli.command()
@click.option('--verbose', '-v', is_flag=True, help='Enable verbose output.')
def hello(verbose: bool) -> None:
    """Say hello to the world."""
    if verbose:
        click.echo("Hello, world! (verbose mode)")
    else:
        click.echo("Hello, world!")


if __name__ == '__main__':
    cli()
