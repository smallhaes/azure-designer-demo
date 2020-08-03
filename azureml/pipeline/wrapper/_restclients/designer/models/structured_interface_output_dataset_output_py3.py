# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .dataset_output_py3 import DatasetOutput


class StructuredInterfaceOutputDatasetOutput(DatasetOutput):
    """StructuredInterfaceOutputDatasetOutput.

    :param dataset_type: Possible values include: 'File', 'Tabular'
    :type dataset_type: str or ~designer.models.DatasetType
    :param dataset_registration:
    :type dataset_registration:
     ~designer.models.DatasetOutputDatasetRegistration
    :param dataset_output_options:
    :type dataset_output_options:
     ~designer.models.DatasetOutputDatasetOutputOptions
    """

    _attribute_map = {
        'dataset_type': {'key': 'datasetType', 'type': 'str'},
        'dataset_registration': {'key': 'datasetRegistration', 'type': 'DatasetOutputDatasetRegistration'},
        'dataset_output_options': {'key': 'datasetOutputOptions', 'type': 'DatasetOutputDatasetOutputOptions'},
    }

    def __init__(self, *, dataset_type=None, dataset_registration=None, dataset_output_options=None, **kwargs) -> None:
        super(StructuredInterfaceOutputDatasetOutput, self).__init__(dataset_type=dataset_type, dataset_registration=dataset_registration, dataset_output_options=dataset_output_options, **kwargs)
