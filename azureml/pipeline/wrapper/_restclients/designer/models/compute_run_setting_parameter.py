# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ComputeRunSettingParameter(Model):
    """ComputeRunSettingParameter.

    :param section_name:
    :type section_name: str
    :param section_description:
    :type section_description: str
    :param name:
    :type name: str
    :param label:
    :type label: str
    :param parameter_type: Possible values include: 'Undefined', 'Int',
     'Double', 'Bool', 'String', 'JsonString'
    :type parameter_type: str or ~designer.models.RunSettingParameterType
    :param is_optional:
    :type is_optional: bool
    :param default_value:
    :type default_value: str
    :param lower_bound:
    :type lower_bound: str
    :param upper_bound:
    :type upper_bound: str
    :param description:
    :type description: str
    :param run_setting_ui_hint:
    :type run_setting_ui_hint:
     ~designer.models.ComputeRunSettingParameterRunSettingUIHint
    :param argument_name:
    :type argument_name: str
    """

    _attribute_map = {
        'section_name': {'key': 'sectionName', 'type': 'str'},
        'section_description': {'key': 'sectionDescription', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'label': {'key': 'label', 'type': 'str'},
        'parameter_type': {'key': 'parameterType', 'type': 'str'},
        'is_optional': {'key': 'isOptional', 'type': 'bool'},
        'default_value': {'key': 'defaultValue', 'type': 'str'},
        'lower_bound': {'key': 'lowerBound', 'type': 'str'},
        'upper_bound': {'key': 'upperBound', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'run_setting_ui_hint': {'key': 'runSettingUIHint', 'type': 'ComputeRunSettingParameterRunSettingUIHint'},
        'argument_name': {'key': 'argumentName', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ComputeRunSettingParameter, self).__init__(**kwargs)
        self.section_name = kwargs.get('section_name', None)
        self.section_description = kwargs.get('section_description', None)
        self.name = kwargs.get('name', None)
        self.label = kwargs.get('label', None)
        self.parameter_type = kwargs.get('parameter_type', None)
        self.is_optional = kwargs.get('is_optional', None)
        self.default_value = kwargs.get('default_value', None)
        self.lower_bound = kwargs.get('lower_bound', None)
        self.upper_bound = kwargs.get('upper_bound', None)
        self.description = kwargs.get('description', None)
        self.run_setting_ui_hint = kwargs.get('run_setting_ui_hint', None)
        self.argument_name = kwargs.get('argument_name', None)
