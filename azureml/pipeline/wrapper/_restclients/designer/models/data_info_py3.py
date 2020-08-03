# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class DataInfo(Model):
    """DataInfo.

    :param id:
    :type id: str
    :param data_source_type: Possible values include: 'None',
     'PipelineDataSource', 'AmlDataset', 'GlobalDataset'
    :type data_source_type: str or ~designer.models.DataSourceType
    :param name:
    :type name: str
    :param description:
    :type description: str
    :param data_type_id:
    :type data_type_id: str
    :param aml_data_store_name:
    :type aml_data_store_name: str
    :param relative_path:
    :type relative_path: str
    :param created_date:
    :type created_date: datetime
    :param created_by_studio:
    :type created_by_studio: bool
    :param data_reference_type: Possible values include: 'None', 'AzureBlob',
     'AzureDataLake', 'AzureFiles', 'AzureSqlDatabase',
     'AzurePostgresDatabase', 'AzureDataLakeGen2', 'DBFS', 'AzureMySqlDatabase'
    :type data_reference_type: str or ~designer.models.DataReferenceType
    :param dataset_type:
    :type dataset_type: str
    :param saved_dataset_id:
    :type saved_dataset_id: str
    :param dataset_version_id:
    :type dataset_version_id: str
    :param connection_string:
    :type connection_string: str
    :param container_name:
    :type container_name: str
    :param data_storage_endpoint_uri:
    :type data_storage_endpoint_uri: str
    :param workspace_sai_token:
    :type workspace_sai_token: str
    :param aml_dataset_data_flow:
    :type aml_dataset_data_flow: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'data_source_type': {'key': 'dataSourceType', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'data_type_id': {'key': 'dataTypeId', 'type': 'str'},
        'aml_data_store_name': {'key': 'amlDataStoreName', 'type': 'str'},
        'relative_path': {'key': 'relativePath', 'type': 'str'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'created_by_studio': {'key': 'createdByStudio', 'type': 'bool'},
        'data_reference_type': {'key': 'dataReferenceType', 'type': 'str'},
        'dataset_type': {'key': 'datasetType', 'type': 'str'},
        'saved_dataset_id': {'key': 'savedDatasetId', 'type': 'str'},
        'dataset_version_id': {'key': 'datasetVersionId', 'type': 'str'},
        'connection_string': {'key': 'connectionString', 'type': 'str'},
        'container_name': {'key': 'containerName', 'type': 'str'},
        'data_storage_endpoint_uri': {'key': 'dataStorageEndpointUri', 'type': 'str'},
        'workspace_sai_token': {'key': 'workspaceSaiToken', 'type': 'str'},
        'aml_dataset_data_flow': {'key': 'amlDatasetDataFlow', 'type': 'str'},
    }

    def __init__(self, *, id: str=None, data_source_type=None, name: str=None, description: str=None, data_type_id: str=None, aml_data_store_name: str=None, relative_path: str=None, created_date=None, created_by_studio: bool=None, data_reference_type=None, dataset_type: str=None, saved_dataset_id: str=None, dataset_version_id: str=None, connection_string: str=None, container_name: str=None, data_storage_endpoint_uri: str=None, workspace_sai_token: str=None, aml_dataset_data_flow: str=None, **kwargs) -> None:
        super(DataInfo, self).__init__(**kwargs)
        self.id = id
        self.data_source_type = data_source_type
        self.name = name
        self.description = description
        self.data_type_id = data_type_id
        self.aml_data_store_name = aml_data_store_name
        self.relative_path = relative_path
        self.created_date = created_date
        self.created_by_studio = created_by_studio
        self.data_reference_type = data_reference_type
        self.dataset_type = dataset_type
        self.saved_dataset_id = saved_dataset_id
        self.dataset_version_id = dataset_version_id
        self.connection_string = connection_string
        self.container_name = container_name
        self.data_storage_endpoint_uri = data_storage_endpoint_uri
        self.workspace_sai_token = workspace_sai_token
        self.aml_dataset_data_flow = aml_dataset_data_flow
