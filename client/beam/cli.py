import asyncclick as click
from aiohttp import ClientSession

SERVER_URL = "http://beam.blakeas.tk"


@click.group()
async def cli():
    pass


@click.argument("file", type=click.File())
@cli.command()
async def send(file):
    """Send files to beam."""
    async with ClientSession() as session:
        response = await session.post(f"{SERVER_URL}/upload", data={"file": file})

        data = await response.json()
        click.echo(data["url"])
