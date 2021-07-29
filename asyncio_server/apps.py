import logging

from server import run_server
from config import read_config

async def main():
    logging.basicConfig(level=logging.DEBUG)

    config = read_config('config.json')
    await run_server(config['port'], config['host'])
