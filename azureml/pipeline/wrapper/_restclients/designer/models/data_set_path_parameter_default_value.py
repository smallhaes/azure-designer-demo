# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .data_set_definition_value import DataSetDefinitionValue


class DataSetPathParameterDefaultValue(DataSetDefinitionValue):
    """DataSetPathParameterDefaultValue.

    :param literal_value:
    :type literal_value: ~designer.models.DataSetDefinitionValueLiteralValue
    :param data_set_reference:
    :type data_set_reference:
     ~designer.models.DataSetDefinitionValueDataSetReference
    :param saved_data_set_reference:
    :type saved_data_set_reference:
     ~designer.models.DataSetDefinitionValueSavedDataSetReference
    """

    _attribute_map = {
        'literal_value': {'key': 'literalValue', 'type': 'DataSetDefinitionValueLiteralValue'},
        'data_set_reference': {'key': 'dataSetReference', 'type': 'DataSetDefinitionValueDataSetReference'},
        'saved_data_set_reference': {'key': 'savedDataSetReference', 'type': 'DataSetDefinitionValueSavedDataSetReference'},
    }

    def __init__(self, **kwargs):
        super(DataSetPathParameterDefaultValue, self).__init__(**kwargs)
