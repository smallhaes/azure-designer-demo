# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ExperimentComputeMetaInfo(Model):
    """ExperimentComputeMetaInfo.

    :param current_node_count:
    :type current_node_count: int
    :param target_node_count:
    :type target_node_count: int
    :param max_node_count:
    :type max_node_count: int
    :param min_node_count:
    :type min_node_count: int
    :param idle_node_count:
    :type idle_node_count: int
    :param running_node_count:
    :type running_node_count: int
    :param preparing_node_count:
    :type preparing_node_count: int
    :param unusable_node_count:
    :type unusable_node_count: int
    :param leaving_node_count:
    :type leaving_node_count: int
    :param preempted_node_count:
    :type preempted_node_count: int
    :param vm_size:
    :type vm_size: str
    :param location:
    :type location: str
    :param provisioning_state:
    :type provisioning_state: str
    :param state:
    :type state: str
    :param os_type:
    :type os_type: str
    :param id:
    :type id: str
    :param name:
    :type name: str
    :param created_by_studio:
    :type created_by_studio: bool
    :param is_gpu_type:
    :type is_gpu_type: bool
    :param resource_id:
    :type resource_id: str
    :param compute_type:
    :type compute_type: str
    """

    _attribute_map = {
        'current_node_count': {'key': 'currentNodeCount', 'type': 'int'},
        'target_node_count': {'key': 'targetNodeCount', 'type': 'int'},
        'max_node_count': {'key': 'maxNodeCount', 'type': 'int'},
        'min_node_count': {'key': 'minNodeCount', 'type': 'int'},
        'idle_node_count': {'key': 'idleNodeCount', 'type': 'int'},
        'running_node_count': {'key': 'runningNodeCount', 'type': 'int'},
        'preparing_node_count': {'key': 'preparingNodeCount', 'type': 'int'},
        'unusable_node_count': {'key': 'unusableNodeCount', 'type': 'int'},
        'leaving_node_count': {'key': 'leavingNodeCount', 'type': 'int'},
        'preempted_node_count': {'key': 'preemptedNodeCount', 'type': 'int'},
        'vm_size': {'key': 'vmSize', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'state': {'key': 'state', 'type': 'str'},
        'os_type': {'key': 'osType', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'created_by_studio': {'key': 'createdByStudio', 'type': 'bool'},
        'is_gpu_type': {'key': 'isGpuType', 'type': 'bool'},
        'resource_id': {'key': 'resourceId', 'type': 'str'},
        'compute_type': {'key': 'computeType', 'type': 'str'},
    }

    def __init__(self, *, current_node_count: int=None, target_node_count: int=None, max_node_count: int=None, min_node_count: int=None, idle_node_count: int=None, running_node_count: int=None, preparing_node_count: int=None, unusable_node_count: int=None, leaving_node_count: int=None, preempted_node_count: int=None, vm_size: str=None, location: str=None, provisioning_state: str=None, state: str=None, os_type: str=None, id: str=None, name: str=None, created_by_studio: bool=None, is_gpu_type: bool=None, resource_id: str=None, compute_type: str=None, **kwargs) -> None:
        super(ExperimentComputeMetaInfo, self).__init__(**kwargs)
        self.current_node_count = current_node_count
        self.target_node_count = target_node_count
        self.max_node_count = max_node_count
        self.min_node_count = min_node_count
        self.idle_node_count = idle_node_count
        self.running_node_count = running_node_count
        self.preparing_node_count = preparing_node_count
        self.unusable_node_count = unusable_node_count
        self.leaving_node_count = leaving_node_count
        self.preempted_node_count = preempted_node_count
        self.vm_size = vm_size
        self.location = location
        self.provisioning_state = provisioning_state
        self.state = state
        self.os_type = os_type
        self.id = id
        self.name = name
        self.created_by_studio = created_by_studio
        self.is_gpu_type = is_gpu_type
        self.resource_id = resource_id
        self.compute_type = compute_type
