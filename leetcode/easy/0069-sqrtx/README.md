# Sqrt(x)

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a non-negative integer `x`, return  *the square root of* `x` *rounded down to the nearest integer*. The returned integer should be  **non-negative**  as well.

You  **must not use**  any built-in exponent function or operator.

- For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

 

 **Example 1:** 

```
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

```

 **Example 2:** 

```
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

```

 

 **Constraints:** 

- 0 <= x <= 231 - 1

## Solution

**Language:** Python  
**Runtime:** 1184 ms (beats 12.72%)  
**Memory:** 19.3 MB (beats 21.72%)  
**Submitted:** 2026-09-07T13:02:28.848Z  

```py
class Solution:
    def mySqrt(self, x: int) -> int:
        i=0
        while i*i<=x:
            i+=1
        return i-1

```

---

[View on LeetCode](https://leetcode.com/problems/sqrtx/)