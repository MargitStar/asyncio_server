import asyncio
import logging

from random import randint, randbytes

async def generate_packet(size):
    begining = b'\xaa\xbb\xcc\xdd'
    ending = b'\xdd\xcc\xbb\xaa'
    sequence = begining + randbytes(size) + ending
    return sequence

async def tcp_echo_client(host, port):
    reader, writer = await asyncio.open_connection(
        host, port)

    packet_size = randint(0,255)
    sequence = await generate_packet(packet_size)
    logging.info(f'Send: {sequence}')

    writer.write(sequence)
    await writer.drain()

    logging.info('Connection closed!')
    writer.close()
    await writer.wait_closed()
