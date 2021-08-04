import asyncio
import logging

from random import choice, randint
from enum import Enum

from asyncio_client.utils import (DataPacket, MultipartPacket, close_connection, write_connection_number)


class Types(str, Enum):
    DATA = 'DataPacket'
    MULTIPART = 'MultipartPacket'

async def write_data_packet_sequence(writer):
    packet_size = randint(0,256)
    packet = DataPacket(packet_size, writer)
    await packet.write_sequence()

async def write_mutipart_packet_sequence(writer):
    packets_amount, packet_size = randint(1,32) ,randint(0,256)
    packet = MultipartPacket(packets_amount, packet_size, writer)
    await packet.write_mp_start()
    await packet.write_mp_body()
    await packet.write_mp_end()

async def write_client(writer, connection):
    data_choice = choice([Types.DATA, Types.MULTIPART])
    await write_connection_number(writer, connection)
    if data_choice == Types.DATA:
        await write_data_packet_sequence(writer)
    elif data_choice == Types.MULTIPART:
        await write_mutipart_packet_sequence(writer)



async def tcp_echo_client(host, port, connection):
    _, writer = await asyncio.open_connection(
        host, port)

    await write_client(writer, connection)
    await close_connection(writer)
    
