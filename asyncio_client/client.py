import asyncio
import logging

from random import choice, randint
from enum import Enum

from asyncio_client.utils import (
    DataPacket,
    MultipartPacket,
    close_connection,
    write_connection_number)


class PacketTypes(str, Enum):
    DATA = 'DataPacket'
    MULTIPART = 'MultipartPacket'


def write_data_packet_sequence(writer):
    packet_size = randint(0, 256)
    packet = DataPacket(packet_size, writer)
    packet.write_sequence()


def write_mutipart_packet_sequence(writer):
    packets_amount, packet_size = randint(1, 32), randint(0, 256)
    packet = MultipartPacket(packets_amount, packet_size, writer)
    packet.write_sequence()


def write_client(writer, connection):
    data_choice = choice([PacketTypes.DATA, PacketTypes.MULTIPART])
    write_connection_number(writer, connection)
    if data_choice == PacketTypes.DATA:
        write_data_packet_sequence(writer)
    elif data_choice == PacketTypes.MULTIPART:
        write_mutipart_packet_sequence(writer)


async def tcp_echo_client(host, port, connection):
    _, writer = await asyncio.open_connection(
        host, port)

    write_client(writer, connection)
    await close_connection(writer)
