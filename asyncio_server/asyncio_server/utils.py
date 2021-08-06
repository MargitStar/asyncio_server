from enum import Enum
from datetime import datetime

from asyncio_db.models import Packet, DataPacket, MultipartPacket, MultipartData
from asyncio_server.fields import StringField, IntField


class DelimiterType(bytes, Enum):
    INTERMEDIATE = b'MPB'
    END = b'MPE'


async def read_data(reader):
    data = await reader.read()
    return data


def convert_data_to_string(connection):
    return connection.decode('utf-8')


class DataParser:
    connection_number = IntField(offset=slice(0, 4))
    data_type = StringField(offset=slice(4, 7))

    def __init__(self, data):
        self.data = data


class DataPacketParser(DataParser):
    def get_dtp_data(self):
        return self.data[7:]

    def write_to_db(self):
        packet = Packet.add(
            type=self.data_type,
            timestamp=datetime.utcnow(),
            client_id=self.connection_number)
        DataPacket.add(data=self.get_dtp_data(), packet=packet)


class MultipartDataParser(DataParser):
    packet_amount = IntField(offset=slice(7, 11))

    def parse_packets(self):
        packet_data = self.data[11:].rstrip(
            DelimiterType.END).split(DelimiterType.INTERMEDIATE)
        packet_data.remove(b'')
        return packet_data

    def write_to_db(self):
        start_packet = Packet.add(
            type=self.data_type,
            timestamp=datetime.utcnow(),
            client_id=self.connection_number)
        saved_packets = [
            Packet.add(
                type=convert_data_to_string(DelimiterType.INTERMEDIATE),
                timestamp=datetime.utcnow(),
                client_id=self.connection_number,
            )
            for _ in range(self.packet_amount)
        ]
        end_packet = Packet.add(
            type=convert_data_to_string(
                DelimiterType.END),
            timestamp=datetime.utcnow(),
            client_id=self.connection_number)
        multipart_packet = MultipartPacket.add(
            start_packet=start_packet, end_packet=end_packet)

        packets = self.parse_packets()
        for idx, packet in enumerate(packets):
            MultipartData.add(
                data=packet,
                idx=idx + 1,
                packet=saved_packets[idx],
                mp_packet=multipart_packet)
