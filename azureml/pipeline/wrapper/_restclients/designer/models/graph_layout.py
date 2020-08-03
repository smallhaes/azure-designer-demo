# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class GraphLayout(Model):
    """GraphLayout.

    :param node_layouts: This is a dictionary
    :type node_layouts: dict[str, ~designer.models.NodeLayout]
    :param id:
    :type id: str
    :param etag:
    :type etag: str
    :param created_date:
    :type created_date: datetime
    :param last_modified_date:
    :type last_modified_date: datetime
    """

    _attribute_map = {
        'node_layouts': {'key': 'nodeLayouts', 'type': '{NodeLayout}'},
        'id': {'key': 'id', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'last_modified_date': {'key': 'lastModifiedDate', 'type': 'iso-8601'},
    }

    def __init__(self, **kwargs):
        super(GraphLayout, self).__init__(**kwargs)
        self.node_layouts = kwargs.get('node_layouts', None)
        self.id = kwargs.get('id', None)
        self.etag = kwargs.get('etag', None)
        self.created_date = kwargs.get('created_date', None)
        self.last_modified_date = kwargs.get('last_modified_date', None)
