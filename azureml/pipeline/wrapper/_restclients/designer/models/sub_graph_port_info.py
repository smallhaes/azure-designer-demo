# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class SubGraphPortInfo(Model):
    """SubGraphPortInfo.

    :param name:
    :type name: str
    :param internal:
    :type internal: list[~designer.models.SubGraphConnectionInfo]
    :param external:
    :type external: list[~designer.models.SubGraphConnectionInfo]
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'internal': {'key': 'internal', 'type': '[SubGraphConnectionInfo]'},
        'external': {'key': 'external', 'type': '[SubGraphConnectionInfo]'},
    }

    def __init__(self, **kwargs):
        super(SubGraphPortInfo, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.internal = kwargs.get('internal', None)
        self.external = kwargs.get('external', None)
