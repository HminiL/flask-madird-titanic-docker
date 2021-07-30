import unittest

from basic.reverse_string import ReverseString


class ReverseStringTest(unittest.TestCase):
    mock = ReverseString()

    def test_str_to_list(self) :
        print(self.mock.str_to_list('hello'))

    def test_reverse_list(self):
        print(self.mock.reverse_list(self.mock.str_to_list('hello')))

    def test_list_to_str(self):
        print(self.mock.list_to_str(self.mock.reverse_list(self.mock.str_to_list('hello'))))

    def test_reverseString(self):
        print(self.mock.reverseString(self.mock.list_to_str(self.mock.reverse_list(self.mock.str_to_list('hello')))))


if __name__ == '__main__':
    unittest.main()