import unittest

from solution import GroupAnagrams


class TestGroupAnagrams(unittest.TestCase):
    def setUp(self):
        self.solution = GroupAnagrams()

    def test_groupAnagrams(self):
        input_data = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expected_output = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
        result = self.solution.groupAnagrams(input_data)
        self.assertEqual(result, expected_output)

    def test_empty_input(self):
        input_data = []
        expected_output = []
        result = self.solution.groupAnagrams(input_data)
        self.assertEqual(result, expected_output)

    def test_single_word(self):
        input_data = ["hello"]
        expected_output = [["hello"]]
        result = self.solution.groupAnagrams(input_data)
        self.assertEqual(result, expected_output)

    def test_multiple_groups(self):
        input_data = ["abc", "def", "bca", "fed", "cab"]
        expected_output = [["abc", "bca", "cab"], ["def", "fed"]]
        result = self.solution.groupAnagrams(input_data)
        self.assertEqual(result, expected_output)


if __name__ == "__main__":
    unittest.main()
