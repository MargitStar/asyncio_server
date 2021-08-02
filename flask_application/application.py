from flask import Flask, render_template

from asyncio_db.models import Packet

app = Flask(__name__)

@app.route('/api/packet')
def packets_list_view():
    packets = Packet.all()
    return render_template('all_packets.html', packets=packets)

@app.route('/api/client/<client_id>/packet')
def client_packets_view(client_id):
    packets = Packet.filtered_by_client_id(client_id=client_id)
    return render_template('all_packets.html', packets=packets)
