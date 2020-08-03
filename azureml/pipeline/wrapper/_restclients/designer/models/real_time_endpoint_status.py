# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class RealTimeEndpointStatus(Model):
    """RealTimeEndpointStatus.

    :param last_operation: Possible values include: 'Create', 'Update',
     'Delete'
    :type last_operation: str or ~designer.models.RealTimeEndpointOpCode
    :param last_operation_status: Possible values include: 'Ongoing',
     'Succeeded', 'Failed', 'SucceededWithWarning'
    :type last_operation_status: str or
     ~designer.models.RealTimeEndpointOpStatusCode
    :param internal_step: Possible values include: 'AboutToDeploy',
     'WaitAksComputeReady', 'RegisterModels', 'CreateServiceFromModels',
     'UpdateServiceFromModels', 'WaitServiceCreating',
     'FetchServiceRelatedInfo', 'TestWithSampleData', 'AboutToDelete',
     'DeleteDeployment', 'DeleteAsset', 'DeleteImage', 'DeleteModel',
     'DeleteServiceRecord'
    :type internal_step: str or
     ~designer.models.RealTimeEndpointInternalStepCode
    :param status_detail:
    :type status_detail: str
    :param deployment_state:
    :type deployment_state: str
    :param service_id:
    :type service_id: str
    :param linked_pipeline_draft_id:
    :type linked_pipeline_draft_id: str
    """

    _attribute_map = {
        'last_operation': {'key': 'lastOperation', 'type': 'str'},
        'last_operation_status': {'key': 'lastOperationStatus', 'type': 'str'},
        'internal_step': {'key': 'internalStep', 'type': 'str'},
        'status_detail': {'key': 'statusDetail', 'type': 'str'},
        'deployment_state': {'key': 'deploymentState', 'type': 'str'},
        'service_id': {'key': 'serviceId', 'type': 'str'},
        'linked_pipeline_draft_id': {'key': 'linkedPipelineDraftId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(RealTimeEndpointStatus, self).__init__(**kwargs)
        self.last_operation = kwargs.get('last_operation', None)
        self.last_operation_status = kwargs.get('last_operation_status', None)
        self.internal_step = kwargs.get('internal_step', None)
        self.status_detail = kwargs.get('status_detail', None)
        self.deployment_state = kwargs.get('deployment_state', None)
        self.service_id = kwargs.get('service_id', None)
        self.linked_pipeline_draft_id = kwargs.get('linked_pipeline_draft_id', None)
