import unittest

from basic.palindrome import Palindrome


class PalindromeTest(unittest.TestCase):

    mock = Palindrome()

    def test_str_to_list(self):
       print(self.mock.str_to_list("race car"))

    def test_isPalindrome(self):
        print(self.mock.isPalindrome(self.mock.str_to_list("hello")))


if __name__ == '__main__':
   unittest.main()