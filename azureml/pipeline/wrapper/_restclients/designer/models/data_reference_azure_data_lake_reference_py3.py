# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .azure_data_lake_reference_py3 import AzureDataLakeReference


class DataReferenceAzureDataLakeReference(AzureDataLakeReference):
    """DataReferenceAzureDataLakeReference.

    :param tenant:
    :type tenant: str
    :param subscription:
    :type subscription: str
    :param resource_group:
    :type resource_group: str
    :param uri:
    :type uri: str
    :param account:
    :type account: str
    :param relative_path:
    :type relative_path: str
    :param aml_data_store_name:
    :type aml_data_store_name: str
    """

    _attribute_map = {
        'tenant': {'key': 'tenant', 'type': 'str'},
        'subscription': {'key': 'subscription', 'type': 'str'},
        'resource_group': {'key': 'resourceGroup', 'type': 'str'},
        'uri': {'key': 'uri', 'type': 'str'},
        'account': {'key': 'account', 'type': 'str'},
        'relative_path': {'key': 'relativePath', 'type': 'str'},
        'aml_data_store_name': {'key': 'amlDataStoreName', 'type': 'str'},
    }

    def __init__(self, *, tenant: str=None, subscription: str=None, resource_group: str=None, uri: str=None, account: str=None, relative_path: str=None, aml_data_store_name: str=None, **kwargs) -> None:
        super(DataReferenceAzureDataLakeReference, self).__init__(tenant=tenant, subscription=subscription, resource_group=resource_group, uri=uri, account=account, relative_path=relative_path, aml_data_store_name=aml_data_store_name, **kwargs)
