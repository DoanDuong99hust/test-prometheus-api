import json
from methods import PrometheusFunctions
from types import SimpleNamespace

with open("data/machine_information.json", "r") as json_file:
	machine_information = json.load(json_file,object_hook=lambda d: SimpleNamespace(**d))

with open("data/data_type.json", "r") as json_file:
	data_type = json.load(json_file,object_hook=lambda d: SimpleNamespace(**d))

prometheus = PrometheusFunctions()

print("Machine: \n 0.local \n 1.worker1 \n 2.worker2")
machine_option = input("Select machine: ")


print("Data wanting to get: \n 1. CPU status \
	\n 2. Network reciever traffic (kb) \
	\n 3. Network transmition traffic (kb)")
target_option = input("Insert target: ")

machine = prometheus.select_machine(machine_option, machine_information)
target_data = prometheus.data_target(target_option, data_type)
prometheus.get_data(machine, target_data)