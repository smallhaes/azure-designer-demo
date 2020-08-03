# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class NodeOutputPort(Model):
    """NodeOutputPort.

    :param name:
    :type name: str
    :param documentation:
    :type documentation: str
    :param data_type_id:
    :type data_type_id: str
    :param pass_through_input_name:
    :type pass_through_input_name: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'documentation': {'key': 'documentation', 'type': 'str'},
        'data_type_id': {'key': 'dataTypeId', 'type': 'str'},
        'pass_through_input_name': {'key': 'passThroughInputName', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(NodeOutputPort, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.documentation = kwargs.get('documentation', None)
        self.data_type_id = kwargs.get('data_type_id', None)
        self.pass_through_input_name = kwargs.get('pass_through_input_name', None)
