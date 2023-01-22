from typing import List

# 给一个有 n 个结点的有向无环图，找到所有从 0 到 n-1 的路径并输出（不要求按顺序）

# 二维数组的第 i 个数组中的单元都表示有向图中 i 号结点所能到达的下一些结点（译者注：有向图是有方向的，即规定了 a→b 你就不能从 b→a ）空就是没有下一个结点了。

import copy

class Solution:

    def dfs(self, graph:List[List[int]], num: int, pre: list, result: list):
        if num == len(graph) - 1:
            pre.append(num)
            result.append(pre)
            
            return
        
        pre.append(num)
    
        for i in graph[num]: 
            temp = copy.copy(pre)   
            
            if i == len(graph) - 1:
                pre.append(i)
                result.append(pre)
            else:
                self.dfs(graph, i, pre, result)
                
            pre = temp
    
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        for x in graph[0]:
            self.dfs(graph, x, [0], result)
            
        return result
            
s = Solution()
graph = [[4,3,1],[3,2,4],[3],[4],[]]

r = s.allPathsSourceTarget(graph)

print(r)
