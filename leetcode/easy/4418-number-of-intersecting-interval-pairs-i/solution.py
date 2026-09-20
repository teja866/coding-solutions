class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        length=len(intervals)
        countofpairs=0
        for i in range(length):
            for j in range(i+1,length):
                start1,end1=intervals[i]
                start2,end2=intervals[j]
                if max(start1,start2)<=min(end1,end2):
                    countofpairs+=1
        return countofpairs