# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class StoredProcedureParameter(Model):
    """StoredProcedureParameter.

    :param name:
    :type name: str
    :param value:
    :type value: str
    :param type: Possible values include: 'String', 'Int', 'Decimal', 'Guid',
     'Boolean', 'Date'
    :type type: str or ~designer.models.StoredProcedureParameterType
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(StoredProcedureParameter, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.value = kwargs.get('value', None)
        self.type = kwargs.get('type', None)
