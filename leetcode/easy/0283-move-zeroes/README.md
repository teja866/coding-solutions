# Move Zeroes

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer array `nums`, move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.

 **Note**  that you must do this in-place without making a copy of the array.

 

 **Example 1:** 

```
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

```

 **Example 2:** 

```
Input: nums = [0]
Output: [0]

```

 

 **Constraints:** 

- 1 <= nums.length <= 104
- -231 <= nums[i] <= 231 - 1

 

 **Follow up:**  Could you minimize the total number of operations done?

## Solution

**Language:** Python  
**Runtime:** 3 ms (beats 81.93%)  
**Memory:** 20.5 MB (beats 25.86%)  
**Submitted:** 2026-09-22T14:49:19.320Z  

```py
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        nonzero=0
        for i in range(n):
            if nums[i]!=0:
                nums[nonzero]=nums[i]
                nonzero+=1
        for i in range(nonzero,n):
            nums[i]=0
```

---

[View on LeetCode](https://leetcode.com/problems/move-zeroes/)