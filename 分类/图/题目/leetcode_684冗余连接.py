from typing import List

# In this problem, a tree is an undirected graph that is connected and has no cycles.
# You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. 
# The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph 
# is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.
# Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, 
# return the answer that occurs last in the input.

# leetcode - 684

class Solution:
    # tc: O(n^2)
    # sc: O(n)
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = _UnionFind(n)

        for edge in edges:
            u = edge[0]
            v = edge[1]

            if uf.is_connected(u,v):
                return edge

            uf.union(u,v)

        return [0,0]

class _UnionFind:
    parent = []

    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def union(self, u, v):
        parent_u = self.find(u)
        parent_v = self.find(v)

        if parent_u == parent_v:
            return

        for i in range(0, len(self.parent)):
            if self.parent[i] == parent_v:
                self.parent[i] = parent_u

    def find(self, x):
        return self.parent[x-1]

    def is_connected(self, u, v):
        return self.find(u) == self.find(v)

edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]
s = Solution()

r = s.findRedundantConnection(edges)

print(r)