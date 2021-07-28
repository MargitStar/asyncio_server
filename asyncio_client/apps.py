import logging

from client import tcp_echo_client
from config import read_config

async def main():
    logging.basicConfig(level=logging.DEBUG)

    config = read_config('config.json')
    await tcp_echo_client(config['port'], config['host'])