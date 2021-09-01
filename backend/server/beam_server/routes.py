from asyncio.protocols import DatagramProtocol
import logging
from aiohttp import web
from uuid import uuid4

api = web.RouteTableDef()

logger = logging.getLogger(__name__)


def file_id_stream():
    while True:
        yield uuid4().hex


file_ids = file_id_stream()


@api.post("/upload")
async def upload_file(request: web.Request) -> web.Response:
    """Upload a file via multi-part."""
    data = await request.post()

    with open(next(file_ids), "wb") as f:
        f.write(data["file"].file.read())

    return web.Response(status=201)


@api.get("/download/{file_id}")
async def download_file(request: web.Request) -> web.Response:
    file_id = request.match_info["file_id"]

    # Need to prevent local file inclustion

    try:
        with open(file_id, "r") as f:
            ...
    except FileNotFoundError:
        return web.Response(status=404, text=f"{file_id=} does not exist.")