import asyncio
import logging

from enum import Enum

from asyncio_server.utils import read_data, DataPacketParser, MultipartDataParser, DataParser

class DataType(str, Enum):
    MULTIPART = 'MPS'
    DATA = 'DTP'
      

async def handle_echo(reader, writer):
    data = await read_data(reader)
    data_parser = DataParser(data)
    if data_parser.parse_data_type() == DataType.DATA:
        parser = DataPacketParser(data)
        parser.write_to_db()
    elif data_parser.parse_data_type() == DataType.MULTIPART:
        parser = MultipartDataParser(data)
        parser.write_to_db()
    logging.info(f"Received {data!r}")
    logging.info("Close the connection")


async def run_server(host, port):
    server = await asyncio.start_server(
        handle_echo, host, port)

    addr = server.sockets[0].getsockname()
    logging.info(f'Serving on {addr}')

    async with server:
        await server.serve_forever()
