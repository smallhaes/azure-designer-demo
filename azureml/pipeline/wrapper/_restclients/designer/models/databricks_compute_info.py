# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class DatabricksComputeInfo(Model):
    """DatabricksComputeInfo.

    :param existing_cluster_id:
    :type existing_cluster_id: str
    """

    _attribute_map = {
        'existing_cluster_id': {'key': 'existingClusterId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(DatabricksComputeInfo, self).__init__(**kwargs)
        self.existing_cluster_id = kwargs.get('existing_cluster_id', None)
