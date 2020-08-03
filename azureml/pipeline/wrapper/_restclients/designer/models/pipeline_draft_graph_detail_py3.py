# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .pipeline_run_graph_detail_py3 import PipelineRunGraphDetail


class PipelineDraftGraphDetail(PipelineRunGraphDetail):
    """PipelineDraftGraphDetail.

    :param graph:
    :type graph: ~designer.models.PipelineRunGraphDetailGraph
    :param graph_nodes_status: This is a dictionary
    :type graph_nodes_status: dict[str, ~designer.models.GraphNodeStatusInfo]
    """

    _attribute_map = {
        'graph': {'key': 'graph', 'type': 'PipelineRunGraphDetailGraph'},
        'graph_nodes_status': {'key': 'graphNodesStatus', 'type': '{GraphNodeStatusInfo}'},
    }

    def __init__(self, *, graph=None, graph_nodes_status=None, **kwargs) -> None:
        super(PipelineDraftGraphDetail, self).__init__(graph=graph, graph_nodes_status=graph_nodes_status, **kwargs)
