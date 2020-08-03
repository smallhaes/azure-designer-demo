# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class RunSettingParameterAssignment(Model):
    """RunSettingParameterAssignment.

    :param use_graph_default_compute:
    :type use_graph_default_compute: bool
    :param mlc_compute_type:
    :type mlc_compute_type: str
    :param compute_run_settings:
    :type compute_run_settings:
     list[~designer.models.RunSettingParameterAssignment]
    :param value_type: Possible values include: 'Literal',
     'GraphParameterName', 'Concatenate', 'Input'
    :type value_type: str or ~designer.models.ParameterValueType
    :param assignments_to_concatenate:
    :type assignments_to_concatenate:
     list[~designer.models.ParameterAssignment]
    :param name:
    :type name: str
    :param value:
    :type value: str
    """

    _attribute_map = {
        'use_graph_default_compute': {'key': 'useGraphDefaultCompute', 'type': 'bool'},
        'mlc_compute_type': {'key': 'mlcComputeType', 'type': 'str'},
        'compute_run_settings': {'key': 'computeRunSettings', 'type': '[RunSettingParameterAssignment]'},
        'value_type': {'key': 'valueType', 'type': 'str'},
        'assignments_to_concatenate': {'key': 'assignmentsToConcatenate', 'type': '[ParameterAssignment]'},
        'name': {'key': 'name', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(RunSettingParameterAssignment, self).__init__(**kwargs)
        self.use_graph_default_compute = kwargs.get('use_graph_default_compute', None)
        self.mlc_compute_type = kwargs.get('mlc_compute_type', None)
        self.compute_run_settings = kwargs.get('compute_run_settings', None)
        self.value_type = kwargs.get('value_type', None)
        self.assignments_to_concatenate = kwargs.get('assignments_to_concatenate', None)
        self.name = kwargs.get('name', None)
        self.value = kwargs.get('value', None)
