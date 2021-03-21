import requests
import json
from types import SimpleNamespace

class PrometheusFunctions():
	"""docstring for PrometheusFunctions"""
	def __init__(self):
		pass

	def select_machine(self, option, machine_information):
		if int(option) == 1 :
			return machine_information.worker1.ip
		elif int(option) == 2 :
			return machine_information.worker2.ip

	def data_target(self, target, data_type):
		if int(target) == 1:
			return data_type.option.cpu_uri
		elif int(target) == 2:
			return data_type.option.network_recieve_uri
		elif int(target) == 3:
			return data_type.option.network_transmit_uri

	def get_data(self, machine, data_type):
		url = "http://"+machine+":5000/api/v1/resources/"+data_type
		response = requests.get(url)
		data = response.text
		parsed = json.loads(data)
		raw_data = json.loads(parsed, object_hook=lambda d: SimpleNamespace(**d))

		list_data = raw_data.data.result
		for i in list_data:
		    print(machine +" - "+ data_type + " : " + i.value[1])
