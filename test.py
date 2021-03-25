from database import getServerStatus as status
from methods import NodeExporterOverride as node_exporter

print(node_exporter.node_cpu_rate())
print(status.get_machine_status())

