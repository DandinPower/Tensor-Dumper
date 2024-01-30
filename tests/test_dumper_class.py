import unittest
import torch
import numpy as np
import os
from dumper import Dumper

class TestDumper(unittest.TestCase):
    def setUp(self):
        self.dumper = Dumper()
        self.filename = 'test.npz'
        self.tensor_fp32 = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
        self.tensor_fp16 = self.tensor_fp32.half()
        self.tensor_int = self.tensor_fp32.int()
        self.tensor_bool = torch.tensor([[True, False], [False, True]])
        self.tensor_large = torch.rand(100000000, dtype=torch.float32)

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_save_load_tensor(self):
        for tensor in [self.tensor_fp32, self.tensor_fp16, self.tensor_int, self.tensor_bool, self.tensor_large]:
            for is_compressed in [True, False]:
                with self.subTest(tensor=tensor, is_compressed=is_compressed):
                    self.dumper.save_tensor(self.filename, tensor, is_compressed)
                    loaded_tensor = self.dumper.load_tensor(self.filename)
                    np.testing.assert_array_equal(loaded_tensor.numpy(), tensor.numpy())
                    os.remove(self.filename)

if __name__ == '__main__':
    unittest.main()