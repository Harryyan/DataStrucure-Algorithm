from typing import List
import heapq

# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], 
# return the minimum number of conference rooms required.

class Solution:
    # tc: O(nlogn)
    # sc: O(n)
    def minMeetingRooms(self,intervals):
        intervals.sort(key=lambda x:x[0])
        n = len(intervals)
        end_list = [intervals[0][1]]
        ans = 1

        for i in range(1,n):
            # 会议开始时间比最早结束的还要早，需增加会议室
            if intervals[i][0]<end_list[0]: 
                ans+=1
                heapq.heappush(end_list, intervals[i][1])
            else: 
                # 可以在最早结束的会议之后开始当前会议，之前的最早结束时间变成当前会议结束的时间
                heapq.heappop(end_list) 
                heapq.heappush(end_list, intervals[i][1])
        return ans   


intervals = [[0,30],[5,10],[15,20]]
s = Solution()

r = s.minMeetingRooms(intervals)
print(r)