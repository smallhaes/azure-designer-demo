# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .created_by_py3 import CreatedBy


class GraphDraftEntityLastUpdatedBy(CreatedBy):
    """GraphDraftEntityLastUpdatedBy.

    :param user_object_id:
    :type user_object_id: str
    :param user_tenant_id:
    :type user_tenant_id: str
    :param user_name:
    :type user_name: str
    """

    _attribute_map = {
        'user_object_id': {'key': 'userObjectId', 'type': 'str'},
        'user_tenant_id': {'key': 'userTenantId', 'type': 'str'},
        'user_name': {'key': 'userName', 'type': 'str'},
    }

    def __init__(self, *, user_object_id: str=None, user_tenant_id: str=None, user_name: str=None, **kwargs) -> None:
        super(GraphDraftEntityLastUpdatedBy, self).__init__(user_object_id=user_object_id, user_tenant_id=user_tenant_id, user_name=user_name, **kwargs)
