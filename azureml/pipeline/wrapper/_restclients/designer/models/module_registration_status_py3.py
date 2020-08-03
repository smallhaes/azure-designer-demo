# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ModuleRegistrationStatus(Model):
    """ModuleRegistrationStatus.

    :param module_name:
    :type module_name: str
    :param status: Possible values include: 'Succeeded', 'Failed'
    :type status: str or ~designer.models.ModuleRegistrationStatusEnum
    :param status_details:
    :type status_details: str
    """

    _attribute_map = {
        'module_name': {'key': 'moduleName', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'status_details': {'key': 'statusDetails', 'type': 'str'},
    }

    def __init__(self, *, module_name: str=None, status=None, status_details: str=None, **kwargs) -> None:
        super(ModuleRegistrationStatus, self).__init__(**kwargs)
        self.module_name = module_name
        self.status = status
        self.status_details = status_details
