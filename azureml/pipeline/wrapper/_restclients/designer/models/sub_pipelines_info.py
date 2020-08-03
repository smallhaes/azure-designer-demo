# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class SubPipelinesInfo(Model):
    """SubPipelinesInfo.

    :param sub_graph_info:
    :type sub_graph_info: list[~designer.models.SubGraphInfo]
    :param node_id_to_sub_graph_id_mapping:
    :type node_id_to_sub_graph_id_mapping: dict[str, str]
    :param sub_pipeline_definition:
    :type sub_pipeline_definition:
     list[~designer.models.SubPipelineDefinition]
    """

    _attribute_map = {
        'sub_graph_info': {'key': 'subGraphInfo', 'type': '[SubGraphInfo]'},
        'node_id_to_sub_graph_id_mapping': {'key': 'nodeIdToSubGraphIdMapping', 'type': '{str}'},
        'sub_pipeline_definition': {'key': 'subPipelineDefinition', 'type': '[SubPipelineDefinition]'},
    }

    def __init__(self, **kwargs):
        super(SubPipelinesInfo, self).__init__(**kwargs)
        self.sub_graph_info = kwargs.get('sub_graph_info', None)
        self.node_id_to_sub_graph_id_mapping = kwargs.get('node_id_to_sub_graph_id_mapping', None)
        self.sub_pipeline_definition = kwargs.get('sub_pipeline_definition', None)
