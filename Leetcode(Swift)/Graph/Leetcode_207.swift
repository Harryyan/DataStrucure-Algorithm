import Foundation

/*
 There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
 You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must
 take course bi first if you want to take course ai.
 
 For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
 Return true if you can finish all courses. Otherwise, return false.
 */

final class Solution_207 {
    
    // 构建 `inDegree`
    func canFinish(_ numCourses: Int, _ prerequisites: [[Int]]) -> Bool {
        var indegree = Counter().inDegree(prerequisites)
        let outdegree = Counter().outDegree(prerequisites)
        
        var queue: [Int] = []
        
        for i in 0..<numCourses {
            if indegree[i] == nil {
                queue.append(i)
            }
        }
        
        var coursesCanTake = queue.count
        
        if coursesCanTake == 0 {
            return false
        }
        
        while queue.count > 0 {
            let index = queue.removeLast()
            let outs = outdegree[index]
            
            if let outs = outs {
                for out in outs {
                    if indegree[out]!.count == 1 {
                        queue.append(out)
                        coursesCanTake += 1
                    } else if indegree[out]!.count > 1 {
                        indegree[out]?.remove(object: index)
                    }
                }
            }
        }
        
        return coursesCanTake == numCourses
    }
}
