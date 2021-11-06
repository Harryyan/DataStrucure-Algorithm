from typing import List

# You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), 
# where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.
# We will send a signal from a given node k. Return the time it takes for all the n nodes to receive the signal. If it is impossible for 
# all the n nodes to receive the signal, return -1.

# leetcode - 743

# 朴素 Dijkstra（邻接矩阵)
class Solution:
    # tc: O(n²)
    # sc: O(n)
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 邻接矩阵 - 范围不大，内存消耗不高 可降低时间复杂度, 操作方便
        g = [[float('inf')] * n for _ in range(n)]
        for x, y, time in times:
            g[x - 1][y - 1] = time

        # 距离数组
        dist = [float('inf')] * n
        dist[k - 1] = 0

        # 标记数组
        used = [False] * n
        for _ in range(n):
            # 找到未标记最近的点
            x = -1
            for y, u in enumerate(used):
                if not u and (x == -1 or dist[y] < dist[x]):
                    x = y
            
            # 更新
            used[x] = True
            for y, time in enumerate(g[x]):
                dist[y] = min(dist[y], dist[x] + time)

        ans = max(dist)
        return ans if ans < float('inf') else -1