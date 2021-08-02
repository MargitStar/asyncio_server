from flask import Flask, jsonify

from asyncio_db.models import Packet

app = Flask(__name__)

@app.route('/api/packet')
def packets_list_view():
    packets = Packet.all()
    return jsonify([packet.serialize for packet in packets])

@app.route('/api/client/<client_id>/packet')
def client_packets_view(client_id):
    packets = Packet.filtered_by_client_id(client_id=client_id)
    return jsonify([packet.serialize for packet in packets])
