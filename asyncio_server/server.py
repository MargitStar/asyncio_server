import asyncio
import logging

from datetime import datetime

from asyncio_db.models import Packet, DataPacket
from asyncio_server.utils import read_data, parse_connection_number, get_packets_amount, get_dtp_data
      

async def handle_echo(reader, writer):
    data = await read_data(reader)
    connection_number, data_type = parse_connection_number(data)
    if data_type == 'DTP':
        recived_data = get_dtp_data(data)
    logging.info(f"Received {data!r}")
    logging.info("Close the connection")


async def run_server(host, port):
    server = await asyncio.start_server(
        handle_echo, host, port)

    addr = server.sockets[0].getsockname()
    logging.info(f'Serving on {addr}')

    async with server:
        await server.serve_forever()
