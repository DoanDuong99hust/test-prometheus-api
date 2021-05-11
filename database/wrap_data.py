from methods import PrometheusFunctions as prometheus
from methods import NodeExporterOverride as node_exporter
import socket as socket


class getServerStatus():

    @staticmethod
    def get_worker():
        worker_data = {
            "name": socket.gethostname(),
            "ip_address": socket.gethostbyname(socket.gethostname())
        }
        return worker_data

    # get cpu data

    @staticmethod
    def get_cpu_data():
        data = c
        cpu_dict_data = {
            "machine_name": socket.gethostname(),
            "value": data
        }
        return cpu_dict_data

    # insert ram data
    @staticmethod
    def get_memory_data():
        data = prometheus.seperate_json_data(node_exporter.node_memory_usage())
        memory_dic_data = {
            "machine": socket.gethostname(),
            "value": data
        }
        return memory_dic_data

    # insert receive-network
    @staticmethod
    def get_receive_net():
        data = prometheus.seperate_json_data(node_exporter.node_network_receive_bytes(device="ens3"))
        receive_dict_data = {
            "machine_name": socket.gethostname(),
            "value": data
        }
        return receive_dict_data

    # insert transmit-network
    @staticmethod
    def get_transmit_net():
        data = prometheus.seperate_json_data(node_exporter.node_network_transmit_bytes(device="ens3"))
        transmit_dict_data = {
            "machine_name": socket.gethostname(),
            "value": data
        }
        return transmit_dict_data

    # insert machine status
    @staticmethod
    def get_machine_status():
        # get cpu data
        cpu_dict = prometheus.seperate_json_data(node_exporter.node_cpu_rate())

        # get memory data
        memory_dict = prometheus.seperate_json_data(node_exporter.node_memory_usage())

        # get receive-net data
        receive_dict = prometheus.seperate_json_data(node_exporter.node_network_receive_bytes())

        # get transmit-net data
        transmit_dict = prometheus.seperate_json_data(node_exporter.node_network_transmit_bytes())

        # get free disk size
        free_disk = prometheus.seperate_json_data(node_exporter.node_filesystem_avail())
        
        status = {
            "machine": socket.gethostname(),
            "cpu": cpu_dict,
            "memory": memory_dict,
            "receive-net": receive_dict,
            "transmit-net": transmit_dict,
            "free-disk": free_disk
        }
        return status
