# 你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。

# 在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，
# 表示如果要学习课程 ai 则 必须 先学习课程  bi 。

# 例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
# 请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。

from typing import DefaultDict, List
from collections import deque

class Solution_TopSort:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites: return True

        inDegree = [0 for _ in range(numCourses)] #只需要存储入度个数即可
        adj = DefaultDict(list)

        for pre in prerequisites:
            inDegree[pre[0]] += 1
            adj[pre[1]].append(pre[0])

        queue = deque()

        for i in range(len(inDegree)):
            if not inDegree[i]:
                queue.append(i)

        while queue:
            node = queue.popleft()
            numCourses -= 1

            for item in adj[node]:
                inDegree[item] -= 1

                if inDegree[item] == 0:
                    queue.append(item)

        return not numCourses
    
so = Solution_TopSort()

result = so.canFinish(4, [[1,0],[2,0],[3,1],[3,2]])
print(result)


print(11 ^ 0)