class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        n=len(intervals)
        count=0
        for i in range(n):
            for j in range(i+1,n):
                a,b=intervals[i]
                c,d=intervals[j]
                if max(a,c)<=min(b,d):
                    count+=1
        return count