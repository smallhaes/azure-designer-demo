# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Storage(Model):
    """Storage.

    :param service_type: Possible values include: 'Undefined', 'Azure',
     'GitHub', 'StorageService', 'StudioPackage'
    :type service_type: str or ~designer.models.StorageType
    :param package_link:
    :type package_link: str
    """

    _attribute_map = {
        'service_type': {'key': 'service_type', 'type': 'str'},
        'package_link': {'key': 'package_link', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Storage, self).__init__(**kwargs)
        self.service_type = kwargs.get('service_type', None)
        self.package_link = kwargs.get('package_link', None)
