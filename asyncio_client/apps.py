import logging
import asyncio
import random 

from client import tcp_echo_client
from config import read_config

   
async def main():
    config = read_config('config.json')

    logging.basicConfig(level=logging.DEBUG)

    for connection in range(config['connections']):
        await tcp_echo_client(config['port'], config['host'])
        await asyncio.sleep(random.randint(1,5))
    