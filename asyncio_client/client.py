import asyncio
import logging


from asyncio_client.utils import write_connection_number, write_sequence, close_connection


async def tcp_echo_client(host, port, connection):
    reader, writer = await asyncio.open_connection(
        host, port)

    await write_connection_number(writer, connection)
    await write_sequence(writer)
    await close_connection(writer)
    
