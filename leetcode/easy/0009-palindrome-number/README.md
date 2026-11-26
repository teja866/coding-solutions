# Palindrome Number

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer `x`, return `true` if `x` is a  **palindrome**, and `false` otherwise.

 

Original
Python3
 **Example 1:** 

```
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

```

 **Example 2:** 

```
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

```

 **Example 3:** 

```
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

```

 

 **Constraints:** 

- -231 <= x <= 231 - 1

 

 **Follow up:**  Could you solve it without converting the integer to a string?

## Solution

**Language:** Python  
**Runtime:** 17 ms (beats 26.69%)  
**Memory:** 19.2 MB (beats 36.22%)  
**Submitted:** 2026-11-26T01:31:48.255Z  

```py
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        n=len(s)
        if x<0:
            return False
        p1=0
        p2=n-1
        while p1<p2:
            if s[p1]!=s[p2]:
                return False
            p1+=1
            p2-=1
        return True
```

---

[View on LeetCode](https://leetcode.com/problems/palindrome-number/)