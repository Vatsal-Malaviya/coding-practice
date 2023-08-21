# Longest Palindromic Substring

![LeetCode Logo](https://leetcode.com/favicon.ico)

This repository contains a solution for the "Longest Palindromic Substring" problem from LeetCode.

## Problem Description
Hash Table | String | Sliding Window

Given a string `s`, find the longest palindromic substring in `s`. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward. Substring means a contiguous sequence of characters within the string.

**Example:**

Input: `"babad"`
Output: `"bab"`
Note: `"aba"` is also a valid answer.

**Example:**

Input: `"cbbd"`
Output: `"bb"`

## Problem Link

For the full problem description and constraints, please refer to the [LeetCode problem page](https://leetcode.com/problems/longest-palindromic-substring/).


## Approach
This solution aims to find the longest palindromic substring in a given string.

1. For each character in the string:
   - Expand around it to find the longest odd palindrome substring.
   - Expand around it and its neighboring character to find the longest even palindrome substring.

2. Maintain a `longest` variable to track the maximum palindrome length.

3. Return the longest palindromic substring found.

The time complexity of this approach is O(n^2) due to nested expansions around potential centers. Optimizations like Manacher's algorithm can achieve linear time complexity.


## Solution

The solution to this problem can be found in the `solution.py` file. It contains a function `longest_palindrome(s: str) -> str` that takes a string as input and returns the longest palindromic substring.

## Testing

Unit tests have been provided to verify the correctness of the solution. You can find these tests in the `tests/test_solution.py` file. To run the tests, use the following command:

```bash
python -m unittest test_solution
