import asyncclick as click


@click.group()
async def cli():
    pass


@click.argument("file", type=click.File(), nargs=-1)
@cli.command()
async def send(file):
    """Send files to beam."""
    click.echo(file)
