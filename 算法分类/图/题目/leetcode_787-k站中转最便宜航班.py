from typing import List
import collections

# There are n cities connected by some number of flights. You are given an array flights where 
# flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.
# You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. 
# If there is no such route, return -1.
# There will not be any multiple flights between two cities.

# leetcode - 787
# SPFA

class Solution:
    # tc: O(edge * vertex)
    # sc: O(n)
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = 10 ** 5
        dist = [INF] * n
        dist[src] = 0
        weight = collections.defaultdict(dict)

        for u, v, w in flights:
            weight[u][v] = w

        queue = collections.deque()
        queue.append([src, -1, 0])
        
        while queue:
            temp = queue.popleft()
            u = temp[0]
            count = temp[1]
            price = temp[2]

            if count + 1 > k:
                break

            for v in weight[u]:
                if price + weight[u][v] < dist[v]:
                    dist[v] = price + weight[u][v]
                    queue.append([v, count+1, dist[v]])

        return dist[dst] if dist[dst] < INF else -1

s = Solution()
n = 4
edges = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]]
src = 0
dst = 3
k = 1

r = s.findCheapestPrice(n, edges, src, dst, k)
print(r)