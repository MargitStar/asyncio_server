import asyncio
import logging

from random import randint, randbytes

logging.basicConfig(level=logging.DEBUG)


async def generate_sequence(number):
    begining = b'\xaa\xbb\xcc\xdd'
    ending = b'\xdd\xcc\xbb\xaa'
    sequence = begining + randbytes(number) + ending
    return sequence

async def tcp_echo_client(host, port):
    reader, writer = await asyncio.open_connection(
        host, port)

    sequence = await generate_sequence(randint(0,255))
    logging.info(f'Send: {sequence}')

    writer.write(sequence)
    await writer.drain()

    logging.info('Connection closed!')
    writer.close()
    await writer.wait_closed()
