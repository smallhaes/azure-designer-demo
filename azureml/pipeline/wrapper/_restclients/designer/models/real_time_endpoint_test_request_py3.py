# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class RealTimeEndpointTestRequest(Model):
    """RealTimeEndpointTestRequest.

    :param end_point:
    :type end_point: str
    :param auth_key:
    :type auth_key: str
    :param payload:
    :type payload: str
    """

    _attribute_map = {
        'end_point': {'key': 'endPoint', 'type': 'str'},
        'auth_key': {'key': 'authKey', 'type': 'str'},
        'payload': {'key': 'payload', 'type': 'str'},
    }

    def __init__(self, *, end_point: str=None, auth_key: str=None, payload: str=None, **kwargs) -> None:
        super(RealTimeEndpointTestRequest, self).__init__(**kwargs)
        self.end_point = end_point
        self.auth_key = auth_key
        self.payload = payload
