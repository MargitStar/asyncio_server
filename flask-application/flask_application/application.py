from flask import Flask, jsonify

from asyncio_db.models import Packet, DataPacket, MultipartData, MultipartPacket
from flask_application.utils import PacketSchema, DataPacketSchema, MultipartDataSchema


app = Flask(__name__)


@app.route('/api/packet/')
def packet_list_view():
    packets = Packet.all()
    packet_schema = PacketSchema()
    return jsonify([packet_schema.dump(packet) for packet in packets])


@app.route('/api/packet/<int:id>/')
def packet_view(id):
    packet = Packet.get_by_id(id)
    packet_schema = PacketSchema()
    return jsonify(packet_schema.dump(packet))


@app.route('/api/dp/')
def packet_list_dp_view():
    data_packets = DataPacket.all()
    data_schema = DataPacketSchema()
    return jsonify([data_schema.dump(data_packet) for data_packet in data_packets])


@app.route('/api/dp/<int:id>/')
def packet_dp_view(id):
    data_packet = DataPacket.get_by_id(id)
    data_schema = DataPacketSchema()
    return jsonify(data_schema.dump(data_packet))


@app.route('/api/mp/')
def packet_list_mp_view():
    result = {}
    multipart_data = MultipartPacket.all()
    mp_packet_id = [data.id for data in multipart_data]
    for packet_id in mp_packet_id:
        mp_packets = MultipartData.filtered_by_idx(packet_id)
        packet = [mp_packet.data for mp_packet in mp_packets]
        result[f'MP_packet_{packet_id}'] = ''.join(packet)
    return result


@app.route('/api/mp/<int:mp_packet_id>/')
def packet_mp_view(mp_packet_id):
    mp_packets = MultipartData.filtered_by_idx(mp_packet_id)
    packet = [mp_packet.data for mp_packet in mp_packets]
    return {'MP_packet': ''.join(packet)}


@app.route('/api/client/<client_id>/packet/')
def client_packets_view(client_id):
    packets = Packet.filtered_by_client_id(client_id=client_id)
    schema = PacketSchema()
    return jsonify([schema.dump(packet) for packet in packets])
