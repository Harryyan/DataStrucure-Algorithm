from typing import List
from collections import defaultdict, deque

# leetcode - 787
# SPFA

class Solution:
    # tc: O(edge * vertex)
    # sc: O(n)
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = 10 ** 5
        prices = [INF] * n
        prices[src] = 0
        graph = defaultdict(dict)  # 二维字典

        for u, v, w in flights:
            graph[u][v] = w

        queue = deque()
        queue.append([src,-1,0])  # [node, count, price]

        while queue:
            node_info = queue.popleft()
            u = node_info[0]
            count = node_info[1]
            price = node_info[2]

            if count > k - 1:
                break

            for v in graph[u]:
                if price + graph[u][v] < prices[v]:
                    prices[v] = price+graph[u][v]
                    queue.append([v,count+1,prices[v]])

        return prices[dst] if prices[dst] < INF else -1

s = Solution()
n = 4
edges = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]]
src = 0
dst = 3
k = 1

r = s.findCheapestPrice(n, edges, src, dst, k)
print(r)