import unittest

from solution import Solution


class TestUniquePaths(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_uniquePaths_top_down(self):
        self.assertEqual(self.solution.uniquePaths(3, 2), 3)
        self.assertEqual(self.solution.uniquePaths(7, 3), 28)

    def test_uniquePaths_bottom_up(self):
        self.assertEqual(self.solution.uniquePaths2(3, 2), 3)
        self.assertEqual(self.solution.uniquePaths2(7, 3), 28)


if __name__ == "__main__":
    unittest.main()
