from typing import List

# In this problem, a tree is an undirected graph that is connected and has no cycles.
# You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. 
# The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph 
# is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.
# Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, 
# return the answer that occurs last in the input.

# leetcode - 684

class Solution:
    # tc: O(nlogn)
    # sc: O(n)
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = _UnionFind(n+1)

        for edge in edges:
            u = edge[0]
            v = edge[1]

            if uf.is_connected(u,v):
                return edge

            uf.union(u,v)

        return [0,0]

class _UnionFind:
    # 初始化并查集
    def __init__(self, n):
        self.parent = {}

        for i in range(n):
            self.parent[i] = i
    
    # 查询root parent
    # 路径压缩
    def find(self, x):
        r = x

        while self.parent[r] != r:
            r = self.parent[r]

        return r

    def union(self, u, v):
        if self.is_connected(u,v): return

        root_u = self.find(u)
        root_v = self.find(v)

        self.parent[root_v] = root_u

    def is_connected(self, u, v):
        return self.find(u) == self.find(v)

edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]
s = Solution()

r = s.findRedundantConnection(edges)

print(r)