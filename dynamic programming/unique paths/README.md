# Unique Paths

![LeetCode Logo](https://leetcode.com/favicon.ico)

This repository contains solutions for the "Unique Paths" problem from LeetCode. Two different approaches are implemented: top-down and bottom-up.

## Problem Description

The "Unique Paths" problem involves finding the number of unique paths from the top-left corner to the bottom-right corner of a `m x n` grid. The robot can only move down or right at any point in time.

**Example:**

Input: `m = 3, n = 2`
Output: `3`

Input: `m = 7, n = 3`
Output: `28`

## Top-Down Approach

The top-down approach uses dynamic programming to compute the number of unique paths. The idea is to populate a matrix `mat` of size `m x n` where `mat[i][j]` represents the number of unique paths to reach position `(i, j)`. The matrix is populated row by row, and each cell is computed by adding the number of paths from the cell above and the cell to the left.

## Bottom-Up Approach

The bottom-up approach uses a recursive function `travel` to compute the number of unique paths. The base cases are when `m` or `n` is equal to 1, in which case there is only one path. For other cases, the function recursively calculates the number of paths by summing the number of paths from the cell above and the cell to the left.

## Testing

Unit tests in `test_solution.py` cover various cases, including examples and edge scenarios.

To run the tests, use:

```bash
python -m unittest test_solution.py