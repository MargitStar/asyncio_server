import asyncio
from datetime import datetime
import logging
from asyncio_db.models import Packet


async def handle_echo(reader, writer):
    data = await reader.readuntil(b'\xdd\xcc\xbb\xaa')
    addr = writer.get_extra_info('peername')

    logging.info(f"Received {data!r} from {addr!r}")
    Packet.add(packet=data, timestamp = datetime.now())

    logging.info("Close the connection")
    writer.close()


async def run_server(host, port):
    server = await asyncio.start_server(
        handle_echo, host, port)

    addr = server.sockets[0].getsockname()
    logging.info(f'Serving on {addr}')

    async with server:
        await server.serve_forever()
