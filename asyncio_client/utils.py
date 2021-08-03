import logging

from random import randbytes, randint

def convert_str_to_bytes(string):
    return f'{string}\n'.encode()


def convert_int_to_bytes(number):
    return bytes([number])


async def generate_dp_packet(size):
    sequence_type = 'DP'
    begining = b'\xaa\xbb\xcc\xdd'
    ending = b'\xdd\xcc\xbb\xaa'
    sequence = begining + randbytes(size) + ending
    return sequence, sequence_type


async def generate_mp_start_packet(size):
    return 'MPS', convert_int_to_bytes(size) + b'MPS'


async def generate_mp_body_packet(size):
    return 'MPB', randbytes(size) + b'MPB'


async def generate_mp_end_packet():
    return 'MPE', b'MPE'


async def write_connection_number(writer, connection):
    writer.write(convert_str_to_bytes(connection))


async def get_sequence():
    packet_size = randint(0,255)
    sequence = await generate_dp_packet(packet_size)
    return sequence


async def write_mp_start(writer):
    packets_amount = randint(1,20)
    start_sequence_type, start_sequence = await generate_mp_start_packet(packets_amount)
    writer.write(convert_str_to_bytes(start_sequence_type))
    writer.write(start_sequence)
    return packets_amount


async def write_mp_body(writer):
    packet_size = randint(0,255)
    body_sequence_type, body_sequence = await generate_mp_body_packet(packet_size)
    writer.write(convert_str_to_bytes(body_sequence_type))
    writer.write(body_sequence)


async def write_mp_end(writer):
    end_sequence_type, end_sequence = await generate_mp_end_packet()
    writer.write(convert_str_to_bytes(end_sequence_type))
    writer.write(end_sequence)   
    

async def write_sequence(writer):
    sequence, sequence_type = await get_sequence()
    logging.info(f'Send: {sequence}')
    writer.write(convert_str_to_bytes(sequence_type))
    writer.write(sequence)
    

async def close_connection(writer):
    await writer.drain()
    logging.info('Connection closed!')
    writer.close()
    await writer.wait_closed()