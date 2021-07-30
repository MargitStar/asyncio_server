import asyncio
import logging

from datetime import datetime

from asyncio_db.models import Packet
from asyncio_server.utils import get_connection_number, read_data
      

async def handle_echo(reader, writer):
    connection, data = await read_data(reader)
    connection_number = get_connection_number(connection)
    
    logging.info(f"Received {data!r}")
    Packet.add(packet=data, timestamp=datetime.now(), client_id=connection_number)
    logging.info("Close the connection")


async def run_server(host, port):
    server = await asyncio.start_server(
        handle_echo, host, port)

    addr = server.sockets[0].getsockname()
    logging.info(f'Serving on {addr}')

    async with server:
        await server.serve_forever()
