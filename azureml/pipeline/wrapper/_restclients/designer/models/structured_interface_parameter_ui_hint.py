# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .ui_parameter_hint import UIParameterHint


class StructuredInterfaceParameterUiHint(UIParameterHint):
    """StructuredInterfaceParameterUiHint.

    :param ui_widget_type: Possible values include: 'Default', 'Mode',
     'ColumnPicker', 'Credential', 'Script'
    :type ui_widget_type: str or ~designer.models.UIWidgetTypeEnum
    :param column_picker:
    :type column_picker: ~designer.models.UIParameterHintColumnPicker
    :param ui_script_language: Possible values include: 'None', 'Python', 'R',
     'Json', 'Sql'
    :type ui_script_language: str or ~designer.models.UIScriptLanguageEnum
    """

    _attribute_map = {
        'ui_widget_type': {'key': 'uiWidgetType', 'type': 'str'},
        'column_picker': {'key': 'columnPicker', 'type': 'UIParameterHintColumnPicker'},
        'ui_script_language': {'key': 'uiScriptLanguage', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(StructuredInterfaceParameterUiHint, self).__init__(**kwargs)
