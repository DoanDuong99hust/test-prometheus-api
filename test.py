from database import getServerStatus as status
from methods import NodeExporterOverride as node_exporter
import json
from types import SimpleNamespace
from methods import PrometheusFunctions as prometheus

# print(node_exporter.node_cpu_rate())
# print(status.get_machine_status())

data = node_exporter.node_cpu_rate()
dict_data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
list_data = dict_data.data.result
for data in list_data:
	data.value[1] = float(data.value[1])
for data in list_data:
	print(data.value)