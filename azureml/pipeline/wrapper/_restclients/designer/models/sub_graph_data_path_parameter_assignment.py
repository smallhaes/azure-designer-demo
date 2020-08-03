# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class SubGraphDataPathParameterAssignment(Model):
    """SubGraphDataPathParameterAssignment.

    :param data_set_path_parameter:
    :type data_set_path_parameter:
     ~designer.models.SubGraphDataPathParameterAssignmentDataSetPathParameter
    :param data_set_path_parameter_assignments:
    :type data_set_path_parameter_assignments: list[str]
    """

    _attribute_map = {
        'data_set_path_parameter': {'key': 'dataSetPathParameter', 'type': 'SubGraphDataPathParameterAssignmentDataSetPathParameter'},
        'data_set_path_parameter_assignments': {'key': 'dataSetPathParameterAssignments', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(SubGraphDataPathParameterAssignment, self).__init__(**kwargs)
        self.data_set_path_parameter = kwargs.get('data_set_path_parameter', None)
        self.data_set_path_parameter_assignments = kwargs.get('data_set_path_parameter_assignments', None)
