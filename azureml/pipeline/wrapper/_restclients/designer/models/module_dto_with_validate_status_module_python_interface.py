# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .module_python_interface import ModulePythonInterface


class ModuleDtoWithValidateStatusModulePythonInterface(ModulePythonInterface):
    """ModuleDtoWithValidateStatusModulePythonInterface.

    :param inputs:
    :type inputs: list[~designer.models.PythonInterfaceMapping]
    :param outputs:
    :type outputs: list[~designer.models.PythonInterfaceMapping]
    :param parameters:
    :type parameters: list[~designer.models.PythonInterfaceMapping]
    """

    _attribute_map = {
        'inputs': {'key': 'inputs', 'type': '[PythonInterfaceMapping]'},
        'outputs': {'key': 'outputs', 'type': '[PythonInterfaceMapping]'},
        'parameters': {'key': 'parameters', 'type': '[PythonInterfaceMapping]'},
    }

    def __init__(self, **kwargs):
        super(ModuleDtoWithValidateStatusModulePythonInterface, self).__init__(**kwargs)
