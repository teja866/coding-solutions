# Pow(x, n)

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Implement pow(x, n), which calculates `x` raised to the power `n` (i.e., `xn`).

 

 **Example 1:** 

```
Input: x = 2.00000, n = 10
Output: 1024.00000

```

 **Example 2:** 

```
Input: x = 2.10000, n = 3
Output: 9.26100

```

 **Example 3:** 

```
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

```

 

 **Constraints:** 

- -100.0 < x < 100.0
- -231 <= n <= 231-1
- n is an integer.
- Either x is not zero or n > 0.
- -104 <= xn <= 104

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.5 MB (beats 56.71%)  
**Submitted:** 2026-09-06T05:59:36.224Z  

```py
class Solution:
    def myPow(self, x: float, n: int) -> float:
        num=1
        if n<0:
            x=1/x
            n=-n
        while n>0:
            #id n is odd, multiply once
            if n%2==1:
                num*=x
            #square the base
            x*=x
            #halve the exponent
            n//=2
        return num
```

---

[View on LeetCode](https://leetcode.com/problems/powx-n/)