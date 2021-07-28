import asyncio
import secrets

from random import randint

async def generate_sequence(number):
    begining = b'\xaa\xbb\xcc\xdd'
    ending = b'\xdd\xcc\xbb\xaa'
    sequence = begining + secrets.token_bytes(number) + ending
    return sequence

async def tcp_echo_client():
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888)

    sequence = await generate_sequence(randint(0,255))

    print(f'Send: {sequence}')
    writer.write(sequence)
    print(111)
    await writer.drain()

    data = await reader.read(300)
    print(f'Received: {data!r}')

    print('Close the connection')
    writer.close()
    await writer.wait_closed()

asyncio.run(tcp_echo_client())