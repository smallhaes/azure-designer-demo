# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AzureMLModuleVersionDescriptor(Model):
    """AzureMLModuleVersionDescriptor.

    :param module_version_id:
    :type module_version_id: str
    :param version:
    :type version: str
    """

    _attribute_map = {
        'module_version_id': {'key': 'moduleVersionId', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
    }

    def __init__(self, *, module_version_id: str=None, version: str=None, **kwargs) -> None:
        super(AzureMLModuleVersionDescriptor, self).__init__(**kwargs)
        self.module_version_id = module_version_id
        self.version = version
