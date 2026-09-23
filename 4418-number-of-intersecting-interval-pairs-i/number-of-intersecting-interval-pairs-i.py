class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        output = 0
        intervals.sort()
        n = len(intervals)
        for i in range(n-1):
            
            for j in range(i+1,n):
                if intervals[i][1]>=intervals[j][0]:
                    output +=1
                else :
                    break
        return output