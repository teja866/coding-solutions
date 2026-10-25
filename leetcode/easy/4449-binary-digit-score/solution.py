class Solution:
    def count_setbitsof(self,n):
        count=0
        while n:
            n=n&(n-1)
            count+=1
        return count
    def calculateScore(self, a: int, b: int) -> int:
        count1=self.count_setbitsof(a)
        count2=self.count_setbitsof(b)
        if count1>=count2:
            return count1*count2
        else:
            return count2//count1