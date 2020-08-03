# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PipelineEndpointSummary(Model):
    """PipelineEndpointSummary.

    :param name:
    :type name: str
    :param description:
    :type description: str
    :param updated_by:
    :type updated_by: str
    :param tags: This is a dictionary
    :type tags: dict[str, str]
    :param entity_status: Possible values include: 'Active', 'Deprecated',
     'Disabled'
    :type entity_status: str or ~designer.models.EntityStatus
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
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'updated_by': {'key': 'updatedBy', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'entity_status': {'key': 'entityStatus', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'last_modified_date': {'key': 'lastModifiedDate', 'type': 'iso-8601'},
    }

    def __init__(self, *, name: str=None, description: str=None, updated_by: str=None, tags=None, entity_status=None, id: str=None, etag: str=None, created_date=None, last_modified_date=None, **kwargs) -> None:
        super(PipelineEndpointSummary, self).__init__(**kwargs)
        self.name = name
        self.description = description
        self.updated_by = updated_by
        self.tags = tags
        self.entity_status = entity_status
        self.id = id
        self.etag = etag
        self.created_date = created_date
        self.last_modified_date = last_modified_date
