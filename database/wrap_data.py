from methods import PrometheusFunctions
from methods import NodeExporterOverride
import socket

prometheus = PrometheusFunctions()
node_exporter = NodeExporterOverride()

hostname = socket.gethostname()
ip_address = socket.gethostbyname()

def get_worker(self, hostname):
	worker_data = {
		"name" : hostname,
		"ip_address" : ip_address
	}
	return worker_data

# get cpu data

def get_cpu_data(self, hostname):
    dict_data = node_exporter.node_exporter.node_cpu_rate(mode="idle")
    data = prometheus.seperate_json_data(data)
    cpu_dict_data = {
        "machine_name": hostname,
        "value": data
    }
    return cpu_dict_data

# insert ram data
# def get_memory_data(hostname):
# 	dict_data = node_exporter.node_exporter.node_cpu_rate(mode="idle")
#     data = prometheus.seperate_json_data(data)
# 	memory_dict_data = {
# 		"machine_name": hostname,
# 		"value": data
# 	}
# 	return memory_dict_data


# insert receive-network
def get_receive_net(self, hostname):
    dict_data = node_exporter.node_exporter.node_network_receive_bytes(device="ens3")
    data = prometheus.seperate_json_data(data)
    receive_dict_data = {
        "machine_name": hostname,
        "value": data
    }
    return receive_dict_data

# insert transmit-network
def get_receive_net(self, hostname):
    dict_data = node_exporter.node_exporter.node_network_transmit_bytes(device="ens3")
    data = prometheus.seperate_json_data(data)
    transmit_dict_data = {
        "machine_name": hostname,
        "value": data
    }
    return transmit_dict_data

# insert machine status
def get_machine_status(self,hostname):
	return "preparing"