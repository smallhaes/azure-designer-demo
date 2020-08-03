# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class EnumParameterRule(Model):
    """EnumParameterRule.

    :param valid_values:
    :type valid_values: list[str]
    """

    _attribute_map = {
        'valid_values': {'key': 'validValues', 'type': '[str]'},
    }

    def __init__(self, *, valid_values=None, **kwargs) -> None:
        super(EnumParameterRule, self).__init__(**kwargs)
        self.valid_values = valid_values
