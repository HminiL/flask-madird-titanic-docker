import unittest

from basic.numpy_lib import Numpy


class NumpyTest(unittest.TestCase):
    mock = Numpy()

    def test_show_numpy(self):
        self.mock.show_numpy()

    def test_numpy_choice(self):
        self.mock.numpy_choice()

    def test_numpy_not_need_for_loop(self):
        self.mock.numpy_not_need_for_loop()

    def test_indexing_slicing(self):
        self.mock.indexing_slicing()

    def test_array_have_type(self):
        self.mock.array_have_one_type()

    def test_np_ones(self):
        self.mock.np_ones()

    def test_np_zero(self):
        self.mock.np_zeros()

    def test_np_eye(self):
        self.mock.np_eye()

    def test_np_array(self):
        self.mock.np_arange()

    def test_np_linspace(self):
        self.mock.np_linspace()

    def test_np_mask(self):
        self.mock.np_mask()

    def test_np_bubble(self):
        self.mock.np_bubble()


if __name__ == '__main__':
    unittest.main()