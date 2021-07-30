import logging
import asyncio
import random 

from asyncio_client.client import tcp_echo_client
from asyncio_client.config import read_config

async def send_packets(port, host, connection):
    while True: 
        try: 
            await tcp_echo_client(port, host, connection)
        except ConnectionRefusedError:
            logging.error("Can't connect to server!")
        sleep_time = random.randint(1,5)
        await asyncio.sleep(sleep_time)

async def main():
    config = read_config('config.json')
    logging.basicConfig(level=logging.DEBUG)

    tasks = [
        asyncio.create_task(send_packets(config['port'], config['host'], connection))
        for connection in range(config['connections'])
    ]
    
    await asyncio.wait(tasks)
