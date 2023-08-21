# Group Anagrams

![LeetCode Logo](https://leetcode.com/favicon.ico)

This repository contains a solution for the "Group Anagrams" problem from LeetCode.

## Problem Description

Given an array of strings, group anagrams together.

An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

**Example:**

Input:
```
["eat", "tea", "tan", "ate", "nat", "bat"]
```

Output:
```
[
   ["eat","tea","ate"],
   ["tan","nat"],
   ["bat"]
]
```
NOTE: Order of output does not matter

## Approach

The solution involves creating a canonical form for each word by sorting its characters. Anagrams will have the same canonical form. A dictionary is then used to group words with the same canonical form together.

The solution follows these steps:
1. Implement a `get_hash` method to generate the canonical form of a word (alternatively use sort method for words less than 100 char length).
2. Iterate through the array of strings and convert each word into its canonical form.
3. Use a dictionary with the canonical form as the key and a list of words as the value to group anagrams.
4. Convert the dictionary values into a list of anagram groups.

## Testing

Unit tests in `test_solution.py` cover various cases, including examples and edge scenarios.

To run the tests, use:

```bash
python -m unittest test_solution.py