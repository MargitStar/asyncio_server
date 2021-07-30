import asyncio
import logging
from types import WrapperDescriptorType
from models import Packet


async def handle_echo(reader, writer):
    data = await reader.read()
    addr = writer.get_extra_info('peername')
    Packet.add(data)

    logging.info(f"Received {data!r} from {addr!r}")

    logging.info("Close the connection")
    writer.close()


async def run_server(host, port):
    server = await asyncio.start_server(
        handle_echo, host, port)

    addr = server.sockets[0].getsockname()
    logging.info(f'Serving on {addr}')

    async with server:
        await server.serve_forever()
