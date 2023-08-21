import unittest

from solution import LongestPalindrome


class TestLongestPalindrome(unittest.TestCase):
    def setUp(self):
        self.longest_palindrome = LongestPalindrome().longest_palindrome

    def test_example_case_1(self):
        self.assertEqual(self.longest_palindrome("babad"), "bab")

    def test_example_case_2(self):
        self.assertEqual(self.longest_palindrome("cbbd"), "bb")

    def test_empty_string(self):
        self.assertEqual(self.longest_palindrome(""), "")

    def test_single_character(self):
        self.assertEqual(self.longest_palindrome("a"), "a")

    def test_even_length_palindrome(self):
        self.assertEqual(self.longest_palindrome("bananas"), "anana")

    def test_odd_length_palindrome(self):
        self.assertEqual(self.longest_palindrome("racecar"), "racecar")


if __name__ == "__main__":
    unittest.main()
