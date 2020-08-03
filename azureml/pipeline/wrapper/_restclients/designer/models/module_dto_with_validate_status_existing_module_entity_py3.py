# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .module_entity_py3 import ModuleEntity


class ModuleDtoWithValidateStatusExistingModuleEntity(ModuleEntity):
    """ModuleDtoWithValidateStatusExistingModuleEntity.

    :param module_execution_type:
    :type module_execution_type: str
    :param module_type: Possible values include: 'None', 'BatchInferencing'
    :type module_type: str or ~designer.models.ModuleType
    :param upload_state: Possible values include: 'Uploading', 'Completed',
     'Canceled', 'Failed'
    :type upload_state: str or ~designer.models.UploadState
    :param is_deterministic:
    :type is_deterministic: bool
    :param structured_interface:
    :type structured_interface:
     ~designer.models.ModuleEntityStructuredInterface
    :param data_location:
    :type data_location: ~designer.models.ModuleEntityDataLocation
    :param identifier_hash:
    :type identifier_hash: str
    :param tags: This is a dictionary
    :type tags: dict[str, str]
    :param properties: This is a dictionary
    :type properties: dict[str, str]
    :param created_by:
    :type created_by: ~designer.models.ModuleEntityCreatedBy
    :param runconfig:
    :type runconfig: str
    :param cloud_settings:
    :type cloud_settings: ~designer.models.ModuleEntityCloudSettings
    :param category:
    :type category: str
    :param step_type:
    :type step_type: str
    :param name:
    :type name: str
    :param hash:
    :type hash: str
    :param description:
    :type description: str
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
        'module_execution_type': {'key': 'moduleExecutionType', 'type': 'str'},
        'module_type': {'key': 'moduleType', 'type': 'str'},
        'upload_state': {'key': 'uploadState', 'type': 'str'},
        'is_deterministic': {'key': 'isDeterministic', 'type': 'bool'},
        'structured_interface': {'key': 'structuredInterface', 'type': 'ModuleEntityStructuredInterface'},
        'data_location': {'key': 'dataLocation', 'type': 'ModuleEntityDataLocation'},
        'identifier_hash': {'key': 'identifierHash', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'properties': {'key': 'properties', 'type': '{str}'},
        'created_by': {'key': 'createdBy', 'type': 'ModuleEntityCreatedBy'},
        'runconfig': {'key': 'runconfig', 'type': 'str'},
        'cloud_settings': {'key': 'cloudSettings', 'type': 'ModuleEntityCloudSettings'},
        'category': {'key': 'category', 'type': 'str'},
        'step_type': {'key': 'stepType', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'hash': {'key': 'hash', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'entity_status': {'key': 'entityStatus', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'last_modified_date': {'key': 'lastModifiedDate', 'type': 'iso-8601'},
    }

    def __init__(self, *, module_execution_type: str=None, module_type=None, upload_state=None, is_deterministic: bool=None, structured_interface=None, data_location=None, identifier_hash: str=None, tags=None, properties=None, created_by=None, runconfig: str=None, cloud_settings=None, category: str=None, step_type: str=None, name: str=None, hash: str=None, description: str=None, entity_status=None, id: str=None, etag: str=None, created_date=None, last_modified_date=None, **kwargs) -> None:
        super(ModuleDtoWithValidateStatusExistingModuleEntity, self).__init__(module_execution_type=module_execution_type, module_type=module_type, upload_state=upload_state, is_deterministic=is_deterministic, structured_interface=structured_interface, data_location=data_location, identifier_hash=identifier_hash, tags=tags, properties=properties, created_by=created_by, runconfig=runconfig, cloud_settings=cloud_settings, category=category, step_type=step_type, name=name, hash=hash, description=description, entity_status=entity_status, id=id, etag=etag, created_date=created_date, last_modified_date=last_modified_date, **kwargs)
