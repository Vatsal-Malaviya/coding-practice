import unittest

from solution import ZigZag


class TestLongestPalindrome(unittest.TestCase):
    def setUp(self):
        self.convert = ZigZag().convert

    def test_example_case_1(self):
        self.assertEqual(self.convert("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR")

    def test_example_case_2(self):
        self.assertEqual(self.convert("PAYPALISHIRING", 4), "PINALSIGYAHRPI")

    def test_empty_string(self):
        self.assertEqual(self.convert("", 2), "")

    def test_single_character(self):
        self.assertEqual(self.convert("A", 1), "A")

    def test_single_row(self):
        self.assertEqual(self.convert("ABC", 1), "ABC")


if __name__ == "__main__":
    unittest.main()
