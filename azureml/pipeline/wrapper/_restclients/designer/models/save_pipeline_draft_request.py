# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class SavePipelineDraftRequest(Model):
    """SavePipelineDraftRequest.

    :param ui_widget_meta_infos:
    :type ui_widget_meta_infos: list[~designer.models.UIWidgetMetaInfo]
    :param web_service_inputs:
    :type web_service_inputs: list[~designer.models.WebServicePort]
    :param web_service_outputs:
    :type web_service_outputs: list[~designer.models.WebServicePort]
    :param nodes_in_draft:
    :type nodes_in_draft: list[str]
    :param module_node_run_settings:
    :type module_node_run_settings:
     list[~designer.models.GraphModuleNodeRunSetting]
    :param name:
    :type name: str
    :param description:
    :type description: str
    :param pipeline_type: Possible values include: 'TrainingPipeline',
     'RealTimeInferencePipeline', 'BatchInferencePipeline', 'Unknown'
    :type pipeline_type: str or ~designer.models.PipelineType
    :param pipeline_draft_mode: Possible values include: 'None', 'Normal',
     'Custom'
    :type pipeline_draft_mode: str or ~designer.models.PipelineDraftMode
    :param graph:
    :type graph: ~designer.models.SavePipelineDraftRequestGraph
    :param tags: This is a dictionary
    :type tags: dict[str, str]
    :param properties: This is a dictionary
    :type properties: dict[str, str]
    :param sub_pipelines_info:
    :type sub_pipelines_info:
     ~designer.models.SavePipelineDraftRequestSubPipelinesInfo
    """

    _attribute_map = {
        'ui_widget_meta_infos': {'key': 'uiWidgetMetaInfos', 'type': '[UIWidgetMetaInfo]'},
        'web_service_inputs': {'key': 'webServiceInputs', 'type': '[WebServicePort]'},
        'web_service_outputs': {'key': 'webServiceOutputs', 'type': '[WebServicePort]'},
        'nodes_in_draft': {'key': 'nodesInDraft', 'type': '[str]'},
        'module_node_run_settings': {'key': 'moduleNodeRunSettings', 'type': '[GraphModuleNodeRunSetting]'},
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'pipeline_type': {'key': 'pipelineType', 'type': 'str'},
        'pipeline_draft_mode': {'key': 'pipelineDraftMode', 'type': 'str'},
        'graph': {'key': 'graph', 'type': 'SavePipelineDraftRequestGraph'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'properties': {'key': 'properties', 'type': '{str}'},
        'sub_pipelines_info': {'key': 'subPipelinesInfo', 'type': 'SavePipelineDraftRequestSubPipelinesInfo'},
    }

    def __init__(self, **kwargs):
        super(SavePipelineDraftRequest, self).__init__(**kwargs)
        self.ui_widget_meta_infos = kwargs.get('ui_widget_meta_infos', None)
        self.web_service_inputs = kwargs.get('web_service_inputs', None)
        self.web_service_outputs = kwargs.get('web_service_outputs', None)
        self.nodes_in_draft = kwargs.get('nodes_in_draft', None)
        self.module_node_run_settings = kwargs.get('module_node_run_settings', None)
        self.name = kwargs.get('name', None)
        self.description = kwargs.get('description', None)
        self.pipeline_type = kwargs.get('pipeline_type', None)
        self.pipeline_draft_mode = kwargs.get('pipeline_draft_mode', None)
        self.graph = kwargs.get('graph', None)
        self.tags = kwargs.get('tags', None)
        self.properties = kwargs.get('properties', None)
        self.sub_pipelines_info = kwargs.get('sub_pipelines_info', None)
