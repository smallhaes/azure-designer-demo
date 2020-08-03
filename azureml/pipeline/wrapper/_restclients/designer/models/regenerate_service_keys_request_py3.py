# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class RegenerateServiceKeysRequest(Model):
    """RegenerateServiceKeysRequest.

    :param key_type: Possible values include: 'Primary', 'Secondary'
    :type key_type: str or ~designer.models.KeyType
    :param key_value:
    :type key_value: str
    """

    _attribute_map = {
        'key_type': {'key': 'keyType', 'type': 'str'},
        'key_value': {'key': 'keyValue', 'type': 'str'},
    }

    def __init__(self, *, key_type=None, key_value: str=None, **kwargs) -> None:
        super(RegenerateServiceKeysRequest, self).__init__(**kwargs)
        self.key_type = key_type
        self.key_value = key_value
