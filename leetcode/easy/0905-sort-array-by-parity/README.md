# Sort Array By Parity

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer array `nums`, move all the even integers at the beginning of the array followed by all the odd integers.

Return  ***any array**  that satisfies this condition*.

 

 **Example 1:** 

```
Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

```

 **Example 2:** 

```
Input: nums = [0]
Output: [0]

```

 

 **Constraints:** 

- 1 <= nums.length <= 5000
- 0 <= nums[i] <= 5000

## Solution

**Language:** Python  
**Runtime:** 2 ms (beats 55.20%)  
**Memory:** 19.9 MB (beats 10.83%)  
**Submitted:** 2026-09-22T15:26:47.204Z  

```py
class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        n=len(nums)
        a=[]
        b=[]
        for i in range(n):
            if nums[i]%2==0:
                a.append(nums[i])
            else:
                b.append(nums[i])
        return a+b
```

---

[View on LeetCode](https://leetcode.com/problems/sort-array-by-parity/)