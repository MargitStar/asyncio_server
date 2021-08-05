import asyncio
import logging

from enum import Enum

from asyncio_server.utils import read_data, DataPacketParser, MultipartDataParser, DataParser


class DataType(str, Enum):
    MULTIPART = 'MPS'
    DATA = 'DTP'

def make_parser(data):
    data_parser = DataParser(data)
    data_type = data_parser.parse_data_type()
    if data_type == DataType.DATA:
        parser = DataPacketParser(data)
    elif data_type == DataType.MULTIPART:
        parser = MultipartDataParser(data)
    else:
        raise ValueError(f'{data_type} is wrong data type!')
    return parser


async def handle_echo(reader, writer):
    data = await read_data(reader)
    parser = make_parser(data)
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
