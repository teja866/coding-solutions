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