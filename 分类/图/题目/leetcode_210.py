# 现在你总共有 n 门课需要选，记为 0 到 n-1。
# 在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]
# 给定课程总量以及它们的先决条件，返回你为了学完所有课程所安排的学习顺序。
# 可能会有多个正确的顺序，你只要返回一种就可以了。如果不可能完成所有课程，返回一个空数组。

from typing import DefaultDict, List

# leetcode - 210
# 图 | 邻接表 | bfs
class Solution:
    # 时间复杂度: O(V*E)
    # 空间复杂度: O(V*E)
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites: 
            return [i for i in range(0, numCourses)]

        # 我依赖谁 | 入度表
        inDeg = DefaultDict(list)
        # 谁依赖我 | 出度表
        outDeg = DefaultDict(list)

        for item in prerequisites:
            inDeg[item[0]].append(item[1])
            outDeg[item[1]].append(item[0])
        
        queue = []
        result = []

        # 搜索无依赖课程
        for item in range(numCourses):
            if len(inDeg[item]) == 0:
                queue.append(item)
        
        # 有环 - 返回空
        if len(queue) == 0:
            return []
        
        while queue:
            item = queue.pop(0)
            result.append(item)
            outs = outDeg[item]

            # 更新队列
            for out in outs:
                if len(inDeg[out]) == 1:
                    queue.append(out)
                elif len(inDeg[out]) > 1:
                    inDeg[out].remove(item)
                   
        return result if len(result) == numCourses else []
    
so = Solution()

prerequisites = [[1,0],[2,0],[3,1],[3,2]]
result = so.findOrder(4, prerequisites)
print(result) 
    