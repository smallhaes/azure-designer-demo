# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class TrainingOutput(Model):
    """TrainingOutput.

    :param training_output_type: Possible values include: 'Metrics', 'Model'
    :type training_output_type: str or ~designer.models.TrainingOutputType
    :param iteration:
    :type iteration: int
    :param metric:
    :type metric: str
    """

    _attribute_map = {
        'training_output_type': {'key': 'trainingOutputType', 'type': 'str'},
        'iteration': {'key': 'iteration', 'type': 'int'},
        'metric': {'key': 'metric', 'type': 'str'},
    }

    def __init__(self, *, training_output_type=None, iteration: int=None, metric: str=None, **kwargs) -> None:
        super(TrainingOutput, self).__init__(**kwargs)
        self.training_output_type = training_output_type
        self.iteration = iteration
        self.metric = metric
