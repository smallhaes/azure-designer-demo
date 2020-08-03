# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .compute_info_py3 import ComputeInfo


class CreateRealTimeEndpointRequestComputeInfo(ComputeInfo):
    """CreateRealTimeEndpointRequestComputeInfo.

    :param name:
    :type name: str
    :param is_ssl_enabled:
    :type is_ssl_enabled: bool
    :param is_gpu_type:
    :type is_gpu_type: bool
    :param cluster_purpose:
    :type cluster_purpose: str
    :param public_ip_address:
    :type public_ip_address: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'is_ssl_enabled': {'key': 'isSslEnabled', 'type': 'bool'},
        'is_gpu_type': {'key': 'isGpuType', 'type': 'bool'},
        'cluster_purpose': {'key': 'clusterPurpose', 'type': 'str'},
        'public_ip_address': {'key': 'publicIpAddress', 'type': 'str'},
    }

    def __init__(self, *, name: str=None, is_ssl_enabled: bool=None, is_gpu_type: bool=None, cluster_purpose: str=None, public_ip_address: str=None, **kwargs) -> None:
        super(CreateRealTimeEndpointRequestComputeInfo, self).__init__(name=name, is_ssl_enabled=is_ssl_enabled, is_gpu_type=is_gpu_type, cluster_purpose=cluster_purpose, public_ip_address=public_ip_address, **kwargs)
