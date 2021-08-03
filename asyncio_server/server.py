import asyncio
import logging

from datetime import datetime

from asyncio_db.models import Packet, DataPacket
from asyncio_server.utils import convert_data_to_string, read_data
      

async def handle_echo(reader, writer):
    connection, data, data_type = await read_data(reader)
    connection_number = convert_data_to_string(connection)
    data_type_str = convert_data_to_string(data_type)
    
    logging.info(f"Received {data!r}")
    packet = Packet.add(type=data_type_str, timestamp=datetime.utcnow(), client_id=connection_number)
    if data_type_str == "DP":
        DataPacket.add(data=data, packet=packet)
    logging.info("Close the connection")


async def run_server(host, port):
    server = await asyncio.start_server(
        handle_echo, host, port)

    addr = server.sockets[0].getsockname()
    logging.info(f'Serving on {addr}')

    async with server:
        await server.serve_forever()
