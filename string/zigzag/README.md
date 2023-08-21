# ZigZag Conversion

![LeetCode Logo](https://leetcode.com/favicon.ico)

This repository contains a solution for the "ZigZag Conversion" problem from LeetCode.

## Problem Description

The "ZigZag Conversion" problem involves converting a given string into a zigzag pattern and then reading the converted pattern line by line. The conversion is done based on the number of rows specified.

**Example:**

Input: `"PAYPALISHIRING", numRows = 3`
Output: `"PAHNAPLSIIGYIR"`


**Example:**

Input: `"PAYPALISHIRING", numRows = 4`
Output: `"PINALSIGYAHRPI"`

**Example:**

Input: `"PAYPALISHIRING", numRows = 1`
Output: `"PAYPALISHIRING"`


## Approach

The solution uses the `ZigZag` class and the `convert` method to create a zigzag pattern based on the specified number of `numRows`.

1. If `numRows` is 1, the input string is returned as is.

2. Initialize an empty list `ans` to store pattern rows.

3. Iterate through each character `c` in the input string `s`:
   - Append `c` to the row at index `i` in `ans`.
   - Update `i` based on direction (`opr`) to simulate zigzag movement.

4. Join rows in `ans` to form the final zigzag pattern.

The solution constructs the zigzag pattern row by row and returns it as a single string.

## Testing

Unit tests in `test_solution.py` cover various cases, including examples and edge scenarios.

To run the tests, use:

```bash
python -m unittest test_solution.py
