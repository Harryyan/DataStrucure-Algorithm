from typing import List


class Solution:
    def isOverlapped(self, last: List[int], interval: List[int]) -> bool:
        return not (last[1] <= interval[0] or last[0] >= interval[1])
        
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        if len(intervals) == 1: return 1
        
        n = len(intervals)
        intervals.sort(key=lambda x: x[0])
        nums = 0
        last = []
        
        for interval in intervals:
            if not last or not self.isOverlapped(last, interval):
                last = interval
                nums += 1
                
                continue
                
            if self.isOverlapped(last, interval):
                if last[-1] > interval[-1]:
                    last = interval
        
        return n-nums
    
nums =  [ [1,5], [2,3], [3,4], [4,6]]
s = Solution()

r = s.eraseOverlapIntervals(nums)

print(r)