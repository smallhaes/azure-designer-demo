# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .hdi_run_configuration import HdiRunConfiguration


class CloudSettingsHdiRunConfig(HdiRunConfiguration):
    """CloudSettingsHdiRunConfig.

    :param file:
    :type file: str
    :param class_name:
    :type class_name: str
    :param files:
    :type files: list[str]
    :param archives:
    :type archives: list[str]
    :param jars:
    :type jars: list[str]
    :param py_files:
    :type py_files: list[str]
    :param compute_name:
    :type compute_name: str
    :param queue:
    :type queue: str
    :param driver_memory:
    :type driver_memory: str
    :param driver_cores:
    :type driver_cores: int
    :param executor_memory:
    :type executor_memory: str
    :param executor_cores:
    :type executor_cores: int
    :param number_executors:
    :type number_executors: int
    :param conf:
    :type conf: dict[str, str]
    :param name:
    :type name: str
    """

    _attribute_map = {
        'file': {'key': 'file', 'type': 'str'},
        'class_name': {'key': 'className', 'type': 'str'},
        'files': {'key': 'files', 'type': '[str]'},
        'archives': {'key': 'archives', 'type': '[str]'},
        'jars': {'key': 'jars', 'type': '[str]'},
        'py_files': {'key': 'pyFiles', 'type': '[str]'},
        'compute_name': {'key': 'computeName', 'type': 'str'},
        'queue': {'key': 'queue', 'type': 'str'},
        'driver_memory': {'key': 'driverMemory', 'type': 'str'},
        'driver_cores': {'key': 'driverCores', 'type': 'int'},
        'executor_memory': {'key': 'executorMemory', 'type': 'str'},
        'executor_cores': {'key': 'executorCores', 'type': 'int'},
        'number_executors': {'key': 'numberExecutors', 'type': 'int'},
        'conf': {'key': 'conf', 'type': '{str}'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(CloudSettingsHdiRunConfig, self).__init__(**kwargs)
