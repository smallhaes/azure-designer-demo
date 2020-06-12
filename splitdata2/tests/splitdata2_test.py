import sys
import unittest
from pathlib import Path

from azureml.core import Workspace
from azureml.pipeline.wrapper import Module

sys.path.append(str(Path(__file__).parent.parent))
from splitdata2 import splitdata2


class TestSplitdata2(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.workspace = Workspace.from_config(str(Path(__file__).parent.parent / 'config.json'))
        cls.base_path = Path(__file__).parent
        cls.outputs = cls.base_path / 'outputs'

    def prepare_inputs(self) -> dict:
        # Change to your own inputs
        return {'input_path': str(self.base_path / 'inputs' / 'input_path')}

    def prepare_parameters(self) -> dict:
        # Change to your own parameters
        return {'str_param': 'some string'}

    def prepare_arguments(self) -> dict:
        # If your input's type is not Path, change this function to your own type.
        result = {}
        inputs = self.prepare_inputs()
        for input in inputs:
            inputs[input] = Path(inputs[input])
        result.update(inputs)
        result.update(self.prepare_parameters())
        return result

    def test_module_from_func(self):
        # This test calls splitdata2 from cmd line arguments.
        local_module = Module.from_func(self.workspace, splitdata2)
        module = local_module()
        module.set_inputs(**self.prepare_inputs())
        module.set_parameters(**self.prepare_parameters())
        status = module.run(working_dir=str(self.outputs), use_docker=True)
        self.assertEqual(status, 'Completed', 'Module run failed.')

    def test_module_func(self):
        # This test calls splitdata2 from parameters directly.
        result = splitdata2(**self.prepare_arguments())
        self.assertIsNotNone(result)
