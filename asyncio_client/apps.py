import logging
import asyncio
import random 

from client import tcp_echo_client
from config import read_config

async def send_packets(port, host):
    while True: 
        try: 
            await tcp_echo_client(port, host)
        except ConnectionRefusedError:
            logging.error("Can't connect to server!")
        await asyncio.sleep(random.randint(1,5))

async def main():
    config = read_config('config.json')
    logging.basicConfig(level=logging.DEBUG)

    tasks = [
        asyncio.create_task(send_packets(config['port'], config['host']))
        for _ in range(config['connections'])
    ]
    
    await asyncio.wait(tasks)
