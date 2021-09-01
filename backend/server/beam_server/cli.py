import asyncio
import logging

import asyncclick as click
from aiohttp import web

from .routes import api


logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.DEBUG)


@click.group()
def cli():
    pass


@click.option(
    "-p",
    "--port",
    type=int,
    default=30777,
)
@click.option("-h", "--host", default="0.0.0.0")
@cli.command()
async def start(host, port):
    app = web.Application()
    app.add_routes(api)

    runner = web.AppRunner(app)

    await runner.setup()
    site = web.TCPSite(runner, host, port)
    await site.start()

    logger.info(f"Serving... {host=}, {port=}")

    while True:
        await asyncio.sleep(3600)
