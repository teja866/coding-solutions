# Valid Anagram

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

 

 **Example 1:** 

 **Input:**  s = "anagram", t = "nagaram"

 **Output:**  true

 **Example 2:** 

 **Input:**  s = "rat", t = "car"

 **Output:**  false

 

 **Constraints:** 

- 1 <= s.length, t.length <= 5 * 104
- s and t consist of lowercase English letters.

 

 **Follow up:**  What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

## Solution

**Language:** Python  
**Runtime:** 11 ms (beats 78.03%)  
**Memory:** 19.4 MB (beats 46.25%)  
**Submitted:** 2026-10-01T10:44:44.823Z  

```py
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt1=[0]*26
        cnt2=[0]*26
        for i in range(len(s)):
            cnt1[ord(s[i])-97]+=1
        for i in range(len(t)):
            cnt2[ord(t[i])-97]+=1
        return cnt1==cnt2
```

---

[View on LeetCode](https://leetcode.com/problems/valid-anagram/)