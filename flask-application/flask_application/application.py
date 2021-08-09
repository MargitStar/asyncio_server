from flask import Flask, jsonify

from asyncio_db.models import Packet
from flask_application.utils import PacketShema

app = Flask(__name__)

@app.route('/api/packet')
def packets_list_view():
    packets = Packet.all()
    schema = PacketShema()
    return jsonify([schema.dump(packet) for packet in packets])

@app.route('/api/client/<client_id>/packet')
def client_packets_view(client_id):
    packets = Packet.filtered_by_client_id(client_id=client_id)
    schema = PacketShema()
    return jsonify([schema.dump(packet) for packet in packets])
