# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .graph_draft_entity import GraphDraftEntity


class SavePipelineDraftRequestGraph(GraphDraftEntity):
    """SavePipelineDraftRequestGraph.

    :param module_nodes:
    :type module_nodes: list[~designer.models.GraphModuleNode]
    :param dataset_nodes:
    :type dataset_nodes: list[~designer.models.GraphDatasetNode]
    :param edges:
    :type edges: list[~designer.models.GraphEdge]
    :param entity_interface:
    :type entity_interface: ~designer.models.GraphDraftEntityEntityInterface
    :param graph_layout:
    :type graph_layout: ~designer.models.GraphDraftEntityGraphLayout
    :param created_by:
    :type created_by: ~designer.models.GraphDraftEntityCreatedBy
    :param last_updated_by:
    :type last_updated_by: ~designer.models.GraphDraftEntityLastUpdatedBy
    :param default_compute:
    :type default_compute: ~designer.models.GraphDraftEntityDefaultCompute
    :param default_datastore:
    :type default_datastore: ~designer.models.GraphDraftEntityDefaultDatastore
    :param id:
    :type id: str
    :param etag:
    :type etag: str
    :param created_date:
    :type created_date: datetime
    :param last_modified_date:
    :type last_modified_date: datetime
    """

    _attribute_map = {
        'module_nodes': {'key': 'moduleNodes', 'type': '[GraphModuleNode]'},
        'dataset_nodes': {'key': 'datasetNodes', 'type': '[GraphDatasetNode]'},
        'edges': {'key': 'edges', 'type': '[GraphEdge]'},
        'entity_interface': {'key': 'entityInterface', 'type': 'GraphDraftEntityEntityInterface'},
        'graph_layout': {'key': 'graphLayout', 'type': 'GraphDraftEntityGraphLayout'},
        'created_by': {'key': 'createdBy', 'type': 'GraphDraftEntityCreatedBy'},
        'last_updated_by': {'key': 'lastUpdatedBy', 'type': 'GraphDraftEntityLastUpdatedBy'},
        'default_compute': {'key': 'defaultCompute', 'type': 'GraphDraftEntityDefaultCompute'},
        'default_datastore': {'key': 'defaultDatastore', 'type': 'GraphDraftEntityDefaultDatastore'},
        'id': {'key': 'id', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'last_modified_date': {'key': 'lastModifiedDate', 'type': 'iso-8601'},
    }

    def __init__(self, **kwargs):
        super(SavePipelineDraftRequestGraph, self).__init__(**kwargs)
