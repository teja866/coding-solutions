class Solution:
    def findMaximumPairs(self, students: str) -> int:
        # write your code here
        n=len(students)
        pairs=[]
        count=0
        for i in range(n-1):
            pair=s[i]+s[i+1]
            paris.append(pair)
        for j in pairs:
            if j in (xy or yx):
                count+=1 
        return count
                