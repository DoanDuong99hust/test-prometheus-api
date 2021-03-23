import pymongo
from methods import PrometheusFunctions
import socket

import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
prometheus = PrometheusFunctions()

hostname = socket.gethostname()

mydb = myclient["test-prometheus"]
worker_tal = mydb["cpu_data"]

print(worker_tal["_id"])


# insert cpu data

@app.route('/api/v1/resources/node-cpu/<hostname>', methods=['POST'])
def set_cpu_data(hostname):
    data = prometheus.get_data("localhost", "node-cpu")
    cpu_tal = mydb["cpu_data"]
    cpu_dict = {
        "machine_name": hostname,
        "value": data
    }
    cpu_tal.insert_one(cpu_dict)
    return "Insert data successful"


# set_cpu_data(hostname)

# insert ram data
ram_tal = mydb["ram_data"]

# insert receive-network
receive_net_tal = mydb["receive_net"]

# insert transmit-network
receive_net_tal = mydb["transmit_net"]

print(mydb.list_collection_names())

worker_data = worker_tal.find()
for x in worker_data:
    print(x)
# app.run()