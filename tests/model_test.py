import unittest
import os
import sys

sys.path.append(os.getcwd())

from src.model import glow_cNF_model
from src.supporting_types import IkflowModelParameters
from src.robots import get_robot

import torch

torch.manual_seed(0)


class ModelTest(unittest.TestCase):
    def test_glow_cNF_model(self):
        """Smoke test - checks that glow_cNF_model() returns"""
        params = IkflowModelParameters()
        robot_model = get_robot("panda_arm")
        model = glow_cNF_model(params, robot_model, dim_cond=7, ndim_tot=9)


if __name__ == "__main__":
    unittest.main()
