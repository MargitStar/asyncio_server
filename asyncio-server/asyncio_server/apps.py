import logging

from asyncio_server.server import run_server
from asyncio_server.config import read_config


async def main():
    logging.basicConfig(level=logging.DEBUG)

    config = read_config('config.json')
    await run_server(config['port'], config['host'])
