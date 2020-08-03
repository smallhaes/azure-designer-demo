# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Stream(Model):
    """Stream.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar can_read:
    :vartype can_read: bool
    :ivar can_seek:
    :vartype can_seek: bool
    :ivar can_timeout:
    :vartype can_timeout: bool
    :ivar can_write:
    :vartype can_write: bool
    :ivar length:
    :vartype length: long
    :param position:
    :type position: long
    :param read_timeout:
    :type read_timeout: int
    :param write_timeout:
    :type write_timeout: int
    """

    _validation = {
        'can_read': {'readonly': True},
        'can_seek': {'readonly': True},
        'can_timeout': {'readonly': True},
        'can_write': {'readonly': True},
        'length': {'readonly': True},
    }

    _attribute_map = {
        'can_read': {'key': 'canRead', 'type': 'bool'},
        'can_seek': {'key': 'canSeek', 'type': 'bool'},
        'can_timeout': {'key': 'canTimeout', 'type': 'bool'},
        'can_write': {'key': 'canWrite', 'type': 'bool'},
        'length': {'key': 'length', 'type': 'long'},
        'position': {'key': 'position', 'type': 'long'},
        'read_timeout': {'key': 'readTimeout', 'type': 'int'},
        'write_timeout': {'key': 'writeTimeout', 'type': 'int'},
    }

    def __init__(self, *, position: int=None, read_timeout: int=None, write_timeout: int=None, **kwargs) -> None:
        super(Stream, self).__init__(**kwargs)
        self.can_read = None
        self.can_seek = None
        self.can_timeout = None
        self.can_write = None
        self.length = None
        self.position = position
        self.read_timeout = read_timeout
        self.write_timeout = write_timeout
