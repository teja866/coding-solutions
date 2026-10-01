class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt1=[0]*26
        cnt2=[0]*26
        for i in range(len(s)):
            cnt1[ord(s[i])-97]+=1
        for i in range(len(t)):
            cnt2[ord(t[i])-97]+=1
        return cnt1==cnt2