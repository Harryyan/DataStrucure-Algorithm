from typing import DefaultDict, List
import math

# 给你一个数组 points ，其中 points[i] = [xi, yi] 表示 X-Y 平面上的一个点。求最多有多少个点在同一条直线上。

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n<3: return n
        res = 0
        for i in range(n-1):
            d = DefaultDict(int)
            d[0] = 0
            same = 1
            for j in range(i+1, n):
                x, y = points[i][0]-points[j][0], points[i][1]-points[j][1]
                if x==0 and y==0:
                    same += 1
                    continue
                if x==0: y = 1
                elif y==0: x = 1
                else:
                    if x<0: x, y = -x, -y
                    g = math.gcd(x, abs(y))
                    x, y = x//g, y//g
                d[(x,y)] += 1
            res = max(res, same+max(d.values()))
        return res