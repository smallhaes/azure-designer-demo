# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .azure_database_reference_py3 import AzureDatabaseReference


class DataReferenceAzurePostgresDatabaseReference(AzureDatabaseReference):
    """DataReferenceAzurePostgresDatabaseReference.

    :param table_name:
    :type table_name: str
    :param sql_query:
    :type sql_query: str
    :param stored_procedure_name:
    :type stored_procedure_name: str
    :param stored_procedure_parameters:
    :type stored_procedure_parameters:
     list[~designer.models.StoredProcedureParameter]
    :param aml_data_store_name:
    :type aml_data_store_name: str
    """

    _attribute_map = {
        'table_name': {'key': 'tableName', 'type': 'str'},
        'sql_query': {'key': 'sqlQuery', 'type': 'str'},
        'stored_procedure_name': {'key': 'storedProcedureName', 'type': 'str'},
        'stored_procedure_parameters': {'key': 'storedProcedureParameters', 'type': '[StoredProcedureParameter]'},
        'aml_data_store_name': {'key': 'amlDataStoreName', 'type': 'str'},
    }

    def __init__(self, *, table_name: str=None, sql_query: str=None, stored_procedure_name: str=None, stored_procedure_parameters=None, aml_data_store_name: str=None, **kwargs) -> None:
        super(DataReferenceAzurePostgresDatabaseReference, self).__init__(table_name=table_name, sql_query=sql_query, stored_procedure_name=stored_procedure_name, stored_procedure_parameters=stored_procedure_parameters, aml_data_store_name=aml_data_store_name, **kwargs)
