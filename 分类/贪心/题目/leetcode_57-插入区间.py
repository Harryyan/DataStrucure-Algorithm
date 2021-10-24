from typing import List

# 给你一个无重叠的 ，按照区间起始端点排序的区间列表。
# 在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）

# leetcode 57

# 时间复杂度: O(n)
# 空间复杂度: O(n)
class Solution:
    def isOverlapped(self, interval: List[int], newInterval: List[int]) -> bool:
        return not (interval[1] < newInterval[0] or interval[0] > newInterval[1])

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals: return [newInterval]
        merged = []
        
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        
        for interval in intervals:
            if not merged or not self.isOverlapped(merged[-1], interval):
                merged.append(interval)
            else:
                merged[-1][0] = min(merged[-1][0], interval[0])
                merged[-1][-1] = max(merged[-1][-1], interval[-1])
                
        return merged
    
    
intervals = []
newInterval = [5,7]

s = Solution()
r = s.insert(intervals, newInterval)

print(r)