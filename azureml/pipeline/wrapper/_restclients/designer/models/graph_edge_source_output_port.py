# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .port_info import PortInfo


class GraphEdgeSourceOutputPort(PortInfo):
    """GraphEdgeSourceOutputPort.

    :param node_id:
    :type node_id: str
    :param port_name:
    :type port_name: str
    :param graph_port_name:
    :type graph_port_name: str
    :param web_service_port:
    :type web_service_port: str
    """

    _attribute_map = {
        'node_id': {'key': 'nodeId', 'type': 'str'},
        'port_name': {'key': 'portName', 'type': 'str'},
        'graph_port_name': {'key': 'graphPortName', 'type': 'str'},
        'web_service_port': {'key': 'webServicePort', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(GraphEdgeSourceOutputPort, self).__init__(**kwargs)
