class Solution:
    def findMaximumPairs(self, students: str) -> int:
        # write your code here
        count=0
        n=len(students)
        i=0
        while i<n-1:
            if (students[i]=='x' and students[i+1]=='y') or (students[i]=='y' and students[i+1]=='x'):
                count+=1 
                i+=2
            else:
                i+=1 
        return count