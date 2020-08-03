# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .datastore_setting_py3 import DatastoreSetting


class SubPipelineDefinitionDefaultDataStore(DatastoreSetting):
    """SubPipelineDefinitionDefaultDataStore.

    :param data_store_name:
    :type data_store_name: str
    """

    _attribute_map = {
        'data_store_name': {'key': 'dataStoreName', 'type': 'str'},
    }

    def __init__(self, *, data_store_name: str=None, **kwargs) -> None:
        super(SubPipelineDefinitionDefaultDataStore, self).__init__(data_store_name=data_store_name, **kwargs)
