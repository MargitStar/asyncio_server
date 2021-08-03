import asyncio
import logging

from random import randint

from asyncio_client.utils import (write_connection_number, write_sequence, close_connection, 
    write_mp_start, write_mp_body, write_mp_end)

async def tcp_echo_client(host, port, connection):
    reader, writer = await asyncio.open_connection(
        host, port)

    choice = randint(1, 2)

    await write_connection_number(writer, connection)
    
    if choice == 1:
        await write_sequence(writer)
    elif choice == 2:
        packet_size = await write_mp_start(writer)
        for _ in range(packet_size):
            await write_mp_body(writer)
        await write_mp_end(writer)
    await close_connection(writer)
    
