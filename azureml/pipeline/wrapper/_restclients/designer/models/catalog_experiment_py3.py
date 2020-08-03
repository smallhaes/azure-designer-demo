# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CatalogExperiment(Model):
    """CatalogExperiment.

    :param id:
    :type id: str
    :param author:
    :type author: ~designer.models.CatalogExperimentAuthor
    :param name:
    :type name: str
    :param summary:
    :type summary: str
    :param hidden:
    :type hidden: bool
    :param owner:
    :type owner: ~designer.models.CatalogExperimentOwner
    :param tags:
    :type tags: list[str]
    :param image_url:
    :type image_url: str
    :param content:
    :type content: ~designer.models.CatalogExperimentContent
    :param algorithms:
    :type algorithms: list[str]
    :param slugs:
    :type slugs: list[str]
    :param etag:
    :type etag: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'author': {'key': 'author', 'type': 'CatalogExperimentAuthor'},
        'name': {'key': 'name', 'type': 'str'},
        'summary': {'key': 'summary', 'type': 'str'},
        'hidden': {'key': 'hidden', 'type': 'bool'},
        'owner': {'key': 'owner', 'type': 'CatalogExperimentOwner'},
        'tags': {'key': 'tags', 'type': '[str]'},
        'image_url': {'key': 'image_url', 'type': 'str'},
        'content': {'key': 'content', 'type': 'CatalogExperimentContent'},
        'algorithms': {'key': 'algorithms', 'type': '[str]'},
        'slugs': {'key': 'slugs', 'type': '[str]'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, *, id: str=None, author=None, name: str=None, summary: str=None, hidden: bool=None, owner=None, tags=None, image_url: str=None, content=None, algorithms=None, slugs=None, etag: str=None, **kwargs) -> None:
        super(CatalogExperiment, self).__init__(**kwargs)
        self.id = id
        self.author = author
        self.name = name
        self.summary = summary
        self.hidden = hidden
        self.owner = owner
        self.tags = tags
        self.image_url = image_url
        self.content = content
        self.algorithms = algorithms
        self.slugs = slugs
        self.etag = etag
