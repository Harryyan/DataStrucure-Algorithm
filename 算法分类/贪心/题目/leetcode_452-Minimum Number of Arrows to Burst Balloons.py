from typing import List

# There are some spherical balloons taped onto a flat wall that represents the XY-plane. 
# The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a 
# balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.
# Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. 
# A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. 
# A shot arrow keeps traveling up infinitely, bursting any balloons in its path.
# Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

# leetcode - 452

class Solution:
    # tc: O(nlogn)
    # sc: 0(1)
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        res = 0
        right = points[0][1]

        for i in range(1, len(points)):
            if points[i][0] <= right:
                right = min(right, points[i][1])
            else:
                res += 1
                right = points[i][1]

        return res + 1

points = [[1,2],[2,3],[3,4],[4,5]]
s = Solution()

r = s.findMinArrowShots(points)

print(r)
