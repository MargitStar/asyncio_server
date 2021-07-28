import asyncio
import logging

from random import randint, randbytes
import random

async def generate_sequence(size):
    begining = b'\xaa\xbb\xcc\xdd'
    ending = b'\xdd\xcc\xbb\xaa'
    sequence = begining + randbytes(size) + ending
    return sequence

async def tcp_echo_client(host, port, connections):
    for i in range(connections):
        reader, writer = await asyncio.open_connection(
            host, port)

        sequence = await generate_sequence(randint(0,255))
        logging.info(f'Send: {sequence}')

        writer.write(sequence)
        await writer.drain()

        logging.info('Connection closed!')
        writer.close()
        await writer.wait_closed()
        await asyncio.sleep(random.randint(1,5))
