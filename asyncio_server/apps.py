import logging

from server import server
from config import read_config

async def main():
    logging.basicConfig(level=logging.DEBUG)

    config = read_config('config.json')
    await server(config['port'], config['host'])
