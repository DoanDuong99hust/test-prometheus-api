
import json
import socket
print(socket.gethostname())
# machine_information = {
# 	"worker1": {"ip" : "192.168.100.94"}, 
# 	"worker2": {"ip" : "192.168.100.94",}
# }

data_type = {
	"option":{
		"cpu_uri": "node-cpu",
		"network_recieve_uri":"network-receive",
		"network_transmit_uri":"network-transmit",
	},
}

# with open('data_type.json', 'w') as json_file:
#   json.dump(data_type, json_file)
