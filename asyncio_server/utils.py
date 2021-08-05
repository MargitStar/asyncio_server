from enum import Enum
from datetime import datetime

from asyncio_db.models import Packet, DataPacket, MultipartPacket, MultipartData

class DelimiterType(bytes, Enum):
    INTERMEDIATE = b'MPB'
    END = b'MPE'


async def read_data(reader):
    data = await reader.read()
    return data

def convert_data_to_string(connection):
    return connection.decode('utf-8')

def convert_data_to_int(number):
    return int.from_bytes(number)


class DataParser:
    def __init__(self, data):
        self.data = data

    def parse_connection_number(self):
        return int(convert_data_to_string(self.data[0:4]))

    def parse_data_type(self):
        return convert_data_to_string(self.data[4:7])


class DataPacketParser(DataParser):
    def get_dtp_data(self):
        return self.data[7:]

    def write_to_db(self):
        client_id = self.parse_connection_number()
        packet = Packet.add(type=self.parse_data_type(), timestamp=datetime.utcnow(), client_id=client_id)
        DataPacket.add(data=self.get_dtp_data(), packet=packet)


class MultipartDataParser(DataParser):
    def parse_packet_amount(self):
        return int(convert_data_to_string(self.data[7:11]))
    
    def parse_packets(self):
        packet_data = self.data[11:].rstrip(DelimiterType.END).split(DelimiterType.INTERMEDIATE)
        packet_data.remove(b'')
        return packet_data
        
    
    def write_to_db(self):
        pack = []
        client_id = self.parse_connection_number()
        start_packet = Packet.add(type=self.parse_data_type(), timestamp=datetime.utcnow(), client_id=client_id)
        packet_amount = self.parse_packet_amount()
        for _ in range(packet_amount):
            pack.append(Packet.add(type=convert_data_to_string(DelimiterType.INTERMEDIATE), timestamp=datetime.utcnow(), client_id=client_id))
        end_packet = Packet.add(type=convert_data_to_string(DelimiterType.END), timestamp=datetime.utcnow(), client_id=client_id)
        multipart_packet = MultipartPacket.add(start_packet=start_packet, end_packet=end_packet)

        packets = self.parse_packets()
        for n in range(packet_amount):
            MultipartData.add(data=packets[n], idx=n+1, packet=pack[n], mp_packet=multipart_packet)