import requests
import json
from types import SimpleNamespace

def select_machine(option):
	if int(option) == 1 :
		return "192.168.100.94"
	elif int(option) == 2 :
		return "192.168.100.208"

def data_target(target):
	if int(target) == 1:
		return "node-cpu"
	elif int(target) == 2:
		return "network-receive"
	elif int(target) == 3:
		return "network-transmit"

def get_data(machine, data_type):
	url = "http://"+machine+":5000/api/v1/resources/"+data_type
	response = requests.get(url)
	data = response.text
	parsed = json.loads(data)
	raw_data = json.loads(parsed, object_hook=lambda d: SimpleNamespace(**d))

	list_data = raw_data.data.result
	for i in list_data:
	    print(machine +"-"+ data_type + ":" + i.value[1])

print("Machine:\n 1.worker1 \n 2.worker2")
machine_option = input("Select machine: ")


print("Data wanting to get: \n 1. CPU status \
	\n 2. Network reciever traffic (kb) \
	\n 3. Network transmition traffic (kb)")
target_option = input("Insert target: ")

get_data(select_machine(machine_option),data_target(target_option))