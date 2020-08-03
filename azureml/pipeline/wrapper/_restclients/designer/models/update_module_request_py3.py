# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class UpdateModuleRequest(Model):
    """UpdateModuleRequest.

    :param module_update_operation_type: Possible values include:
     'SetDefaultVersion', 'EnableModule', 'DisableModule'
    :type module_update_operation_type: str or
     ~designer.models.ModuleUpdateOperationType
    :param module_version:
    :type module_version: str
    """

    _attribute_map = {
        'module_update_operation_type': {'key': 'moduleUpdateOperationType', 'type': 'str'},
        'module_version': {'key': 'moduleVersion', 'type': 'str'},
    }

    def __init__(self, *, module_update_operation_type=None, module_version: str=None, **kwargs) -> None:
        super(UpdateModuleRequest, self).__init__(**kwargs)
        self.module_update_operation_type = module_update_operation_type
        self.module_version = module_version
