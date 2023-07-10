from collections import List,defaultdict, deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        inDeg = defaultdict(int)
        queue = []

        # 构建图
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            inDeg[edge[0]] += 1
            inDeg[edge[1]] += 1

        # 寻找入度为1的节点
        for (u,v) in inDeg.items():
            if v == 1: queue.append(u)

        count = len(queue)
        if count == 0: return [0]

        while count < n:
            newQueue = []

            for item in queue:
                for u in graph[item]:
                    inDeg[u] -= 1

                    if inDeg[u] == 1: newQueue.append(u)

            count += len(newQueue)
            queue = newQueue

        return queue