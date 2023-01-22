import heapq, collections
from typing import List

# 单源最短路径

class Dijkstra:
    def startwith(self, start: int, matrix: list) -> list:
        '''
        单源最短路径实现(稠密图)

        稠密图使用邻接矩阵为佳: edge≈node^2

        Args:
            start: 起点
            matrix: 邻接矩阵，表示点和点之间的距离
        '''
        visited = [start]
        non_visited = [x for x in range(len(matrix)) if x != start]
        
        shortest_dis= matrix[start]
        
        while non_visited:
            idx = non_visited[0]

            for i in non_visited:
                if shortest_dis[i] < shortest_dis[idx]: idx = i

            non_visited.remove(idx)
            visited.append(idx)

            for i in non_visited:
                dis = shortest_dis[idx] + matrix[idx][i]

                if dis < shortest_dis[i]: shortest_dis[i] = dis

        return shortest_dis 

    # 堆优化 - 未处理负权边
    # tc: O(edge*logV)
    # sc: O(edge)
    def dijkstra(self, G,start): 
        '''
        G = {   1: {1:0,    2:1,    3:12},
                2: {2:0,    3:9,    4:3},
                3: {3:0,    5:5},
                4: {3:4,    4:0,    5:13,   6:15},
                5: {5:0,    6:4},
                6: {6:0}}
        '''

        INF = 999999999
    
        dis = dict((key,INF) for key in G)    # start到每个点的距离
        dis[start] = 0
        vis = dict((key,False) for key in G)    #是否访问过，1位访问过，0为未访问
        pq = []    #存放排序后的值
        heapq.heappush(pq,[dis[start],start])
    
        path = dict((key,[start]) for key in G)    #记录到每个点的路径
        while len(pq)>0:
            v_dis,v = heapq.heappop(pq)    #未访问点中距离最小的点和对应的距离
            if vis[v] == True:
                continue
            vis[v] = True
            p = path[v].copy()    #到v的最短路径
            for node in G[v]:    #与v直接相连的点
                new_dis = dis[v] + float(G[v][node])
                if new_dis < dis[node] and (not vis[node]):    #如果与v直接相连的node通过v到src的距离小于dis中对应的node的值,则用小的值替换
                    dis[node] = new_dis    #更新点的距离
                #  dis_un[node][0] = new_dis    #更新未访问的点到start的距离
                    heapq.heappush(pq,[dis[node],node])
                    temp = p.copy()
                    temp.append(node)    #更新node的路径

    # 平均tc: O(edge * vertex)
    # sc: O(v)
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        dist = [float("inf") for _ in range(N)]
        K -= 1
        dist[K] = 0
        weight = collections.defaultdict(dict)
        for u, v, w in times:
            weight[u-1][v-1] = w
        queue = collections.deque([K])
        while queue:
            u = queue.popleft()
            for v in weight[u]:
                if dist[u] + weight[u][v] < dist[v]:
                    dist[v] = dist[u] + weight[u][v]
                    queue.append(v)
        return max(dist) if max(dist) < float("inf") else -1
   

    

inf = 996
matrix = [[0, 1, 12, inf, inf, inf],
              [inf, 0, 9, 3, inf, inf],
              [inf, inf, 0, inf, 5, inf],
              [inf, inf, 4, 0, 13, 15],
              [inf, inf, inf ,inf, 0, 4],
              [inf, inf, inf, inf ,inf, 0]]

s = Dijkstra()

r = s.startwith(0, matrix)
print(r)