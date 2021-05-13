from prometheus_http_client import NodeExporter
from prometheus_http_client.prometheus import relabel


class NodeExporterOverride(NodeExporter):

    @relabel('100 - (avg by (instance, job) (irate(node_cpu{mode="idle"}[10m])) * 100)')
    def node_cpu_rate(self, **kwargs):
        pass

    @relabel('irate(node_network_receive_bytes{device="wlp2s0"}[5m])/1024')
    def node_network_receive_bytes(self, **kwargs):
        pass

    @relabel('irate(node_network_transmit_bytes{device="wlp2s0"}[5m])/1024')
    def node_network_transmit_bytes(self, **kwargs):
        pass

    @relabel('((avg_over_time(node_memory_MemTotal[5m]) - avg_over_time(node_memory_MemFree[5m]) - avg_over_time('
             'node_memory_Cached[5m]) - avg_over_time(node_memory_Buffers[5m])) / avg_over_time(node_memory_MemTotal['
             '5m])) * 100')
    def node_memory_usage(self):
        pass

    @relabel('(node_filesystem_avail{mountpoint="/",fstype="ext4"})/1024')
    def node_filesystem_avail(self, **kwargs):
        pass