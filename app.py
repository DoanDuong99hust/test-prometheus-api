from methods import *

import socket

import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
node_exporter = NodeExporterOverride()


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


@app.route('/api/v1/resources/node-cpu', methods=['GET'])
def cpu_data():
    data = node_exporter.node_cpu_rate(mode="idle")
    return jsonify(data)


@app.route('/api/v1/resources/network-receive', methods=['GET'])
def network_receive_data():
    data = node_exporter.node_network_receive_bytes(device="wlp2s0")
    return jsonify(data)

@app.route('/api/v1/resources/network-transmit', methods=['GET'])
def network_transmit_data():
    data = node_exporter.node_network_transmit_bytes(device="wlp2s0")
    return jsonify(data)

app.run(host="192.168.100.94")

