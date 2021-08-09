from flask import Flask, jsonify

from asyncio_db.models import Packet, DataPacket
from flask_application.utils import PacketSchema, DataPacketSchema

app = Flask(__name__)

@app.route('/api/dtp/packet')
def packets_list_dtp_view():
    data_packets = DataPacket.all()
    data_schema = DataPacketSchema()
    return jsonify([data_schema.dump(data_packet) for data_packet in data_packets])

@app.route('/api/client/<client_id>/packet')
def client_packets_view(client_id):
    packets = Packet.filtered_by_client_id(client_id=client_id)
    schema = PacketSchema()
    return jsonify([schema.dump(packet) for packet in packets])
