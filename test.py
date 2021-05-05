
import json
import socket
from methods import PrometheusFunctions
from types import SimpleNamespace
import requests
print(socket.gethostname())

data_type = {
	"option":{
		"cpu_uri": "node-cpu",
		"network_recieve_uri":"network-receive",
		"network_transmit_uri":"network-transmit",
	},
}

url = "http://127.0.0.1:5000/api/v1/resources/cluster_node_list"
response = requests.get(url)
data = response.text
parsed = json.loads(data)
raw_data = json.loads(parsed, object_hook=lambda d: SimpleNamespace(**d))

print(parsed.data)
for i in parsed:
	# list_data = i.metric
	# print(i)
	pass