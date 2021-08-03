import logging

from random import randbytes, randint

def convert_str_to_bytes(string):
    return f'{string}\n'.encode()

async def generate_packet(size):
    sequence_type = 'DP'
    begining = b'\xaa\xbb\xcc\xdd'
    ending = b'\xdd\xcc\xbb\xaa'
    sequence = begining + randbytes(size) + ending
    return sequence, sequence_type

async def write_connection_number(writer, connection):
    writer.write(convert_str_to_bytes(connection))

async def get_sequence():
    packet_size = randint(0,255)
    sequence = await generate_packet(packet_size)
    return sequence

async def write_sequence(writer):
    sequence, sequence_type = await get_sequence()
    logging.info(f'Send: {sequence}')
    writer.write(sequence)
    writer.write(convert_str_to_bytes(sequence_type))

async def close_connection(writer):
    await writer.drain()
    logging.info('Connection closed!')
    writer.close()
    await writer.wait_closed()