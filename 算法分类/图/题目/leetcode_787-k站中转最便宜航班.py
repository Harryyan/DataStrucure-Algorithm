from typing import List
from collections import defaultdict, deque
import heapq

class Solution_Dijkstra:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = 10 ** 5
        graph = defaultdict(dict)
        visit = [n+1]*n

        for u,v,w in flights:
            graph[u][v] = w

        pq = [[0, src, 0]] # [price, node, count]
        heapq.heapify(pq)

        while pq:
            price,u,count = heapq.heappop(pq)

            if u == dst: return price
            if count > k or visit[u] <= count: # 使用最小堆需要记录当前节点访问次数
                continue

            visit[u] = count
            for v in graph[u]:
                # 无需判断是否小于当前prices[v]
                heapq.heappush(pq,[price + graph[u][v],v,count+1])
        return -1

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
            u, count, price = node_info

            if count > k - 1:
                break

            for v in graph[u]:
                # 需判断是否小于当前prices[v]
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