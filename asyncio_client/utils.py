import logging

from random import randbytes, randint


def convert_str_to_bytes(string):
    return string.encode()


def convert_int_to_bytes(number):
    return bytes([number])


async def close_connection(writer):
    await writer.drain()
    logging.info('Connection closed!')
    writer.close()
    await writer.wait_closed()


def write_connection_number(writer, connection):
    writer.write(convert_str_to_bytes(str(connection).zfill(4)))


class DataPacket:
    def __init__(self, packet_size, writer):
        self.packet_size = packet_size
        self.writer = writer

    def generate_dp_packet(self):
        return b'DTP' + randbytes(self.packet_size)

    def write_sequence(self):
        sequence = self.generate_dp_packet()
        logging.info(f'Send: {sequence}')
        self.writer.write(sequence)


class MultipartPacket:
    def __init__(self, packets_amount, packet_size, writer):
        self.packets_amount = packets_amount
        self.packet_size = packet_size
        self.writer = writer

    def generate_mp_start_packet(self):
        return f'MPS{self.packets_amount:04}'.encode()

    def generate_mp_body_packet(self):
        return b'MPB' + randbytes(self.packet_size)

    def generate_mp_end_packet(self):
        return 'MPE'.encode()

    def write_mp_start(self):
        start_sequence = self.generate_mp_start_packet()
        self.writer.write(start_sequence)

    def write_mp_body(self):
        for _ in range(self.packets_amount):
            body_sequence = self.generate_mp_body_packet()
            self.writer.write(body_sequence)

    def write_mp_end(self):
        end_sequence = self.generate_mp_end_packet()
        self.writer.write(end_sequence)

    def write_sequence(self):
        self.write_mp_start()
        self.write_mp_body()
        self.write_mp_end()
