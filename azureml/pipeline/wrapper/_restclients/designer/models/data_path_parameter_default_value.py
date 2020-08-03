# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .legacy_data_path import LegacyDataPath


class DataPathParameterDefaultValue(LegacyDataPath):
    """DataPathParameterDefaultValue.

    :param data_store_name:
    :type data_store_name: str
    :param relative_path:
    :type relative_path: str
    """

    _attribute_map = {
        'data_store_name': {'key': 'dataStoreName', 'type': 'str'},
        'relative_path': {'key': 'relativePath', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(DataPathParameterDefaultValue, self).__init__(**kwargs)
