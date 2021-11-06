# 你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。

# 在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，
# 表示如果要学习课程 ai 则 必须 先学习课程  bi 。

# 例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
# 请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。

from typing import DefaultDict, List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites: return True
        
        finalNumbers = 0

        # 我依赖谁
        inDeg = DefaultDict(list)
        # 谁依赖我
        outDeg = DefaultDict(list)

        for item in prerequisites:
            inDeg[item[0]].append(item[1])
            outDeg[item[1]].append(item[0])
        
        queue = []
        for item in range(0, numCourses):
            if len(inDeg[item]) == 0:
                queue.append(item)
        
        finalNumbers += len(queue)
        
        if len(queue) == 0:
            return False
        
        while queue:
            item = queue.pop(0)
            outs = outDeg[item]
            
            print(item, end="\t")

            for out in outs:
                if len(inDeg[out]) == 1:
                    queue.append(out)
                    finalNumbers += 1
                elif len(inDeg[out]) > 1:
                    inDeg[out].remove(item)
                  
        return finalNumbers == numCourses


so = Solution()

result = so.canFinish(4, [[1,0],[2,0],[3,1],[3,2]])
print(result)


print(11 ^ 0)