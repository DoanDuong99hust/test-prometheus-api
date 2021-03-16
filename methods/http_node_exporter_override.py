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
