import logging
import asyncio
import random 

from client import tcp_echo_client
from config import read_config

async def run_server(port, host):
    while True: 
        await tcp_echo_client(port, host)
        await asyncio.sleep(random.randint(1,5))

async def main():
    config = read_config('config.json')
    logging.basicConfig(level=logging.DEBUG)

    tasks = [
        asyncio.create_task(run_server(config['port'], config['host']))
        for connection in range(config['connections'])
    ]

    await asyncio.wait(tasks)
