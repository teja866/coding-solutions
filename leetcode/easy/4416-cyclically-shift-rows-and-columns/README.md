# Q1. Cyclically Shift Rows and Columns

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You are given an integer `n`, a 2D integer array `grid` of size `n x n`, and two integer arrays `rowShift` and `colShift`, each of length `n` where:

- rowShift[i] represents the number of positions to cyclically left shift the ith row of grid.
- colShift[j] represents the number of positions to cyclically upward shift the jth column of grid.

First, cyclically shift each row according to `rowShift`, then cyclically shift each column according to `colShift`.

Return the resulting grid after performing all the shifts.

A  **cyclic left shift**  of the `ith` row by `k` positions shifts only that row. The element at column `j` moves to column `(j - k + n) % n`, while all other rows remain unchanged.

A  **cyclic upward shift**  of the `jth` column by `k` positions shifts only that column. The element at row `i` moves to row `(i - k + n) % n`, while all other columns remain unchanged.

 

 **Example 1:** 

 **Input:**  n = 2, `grid` = [[1,2],[3,4]], rowShift = [1,0], colShift = [0,1]

 **Output:**  [[2,4],[3,1]]

 **Explanation:** 

The `grid` changes as follows:

 **Example 2:** 

 **Input:**  n = 3, `grid` = [[1,2,3],[4,5,6],[7,8,9]], rowShift = [1,2,0], colShift = [2,2,1]

 **Output:**  [[7,8,5],[2,3,9],[6,4,1]]

 **Explanation:** 

The `grid` changes as follows:

 

 **Constraints:** 

- 1 <= n == grid.length == grid[i].length <= 10
- 1 <= grid[i][j] <= 100
- rowShift.length == colShift.length == n
- 0 <= rowShift[i], colShift[i] < n

## Solution

**Language:** Python  
**Runtime:** 11 ms (beats 100.00%)  
**Memory:** 19.5 MB (beats 100.00%)  
**Submitted:** 2026-09-13T02:48:17.459Z  

```py
class Solution:
    def cyclicShift(self, n: int, grid: list[list[int]], rowShift: list[int], colShift: list[int]) -> list[list[int]]:
        for i in range(n):
            k=rowShift[i]
            new_row=[0]*n
            for j in range(n):
                new_row[(j-k+n)%n]=grid[i][j]
            grid[i]=new_row

        for j in range(n):
            k=colShift[j]
            new_col=[0]*n
            for i in range(n):
                new_col[(i-k+n)%n]=grid[i][j]
            for i in range(n):
                grid[i][j]=new_col[i]

        return grid
```

---

[View on LeetCode](https://leetcode.com/problems/cyclically-shift-rows-and-columns/)