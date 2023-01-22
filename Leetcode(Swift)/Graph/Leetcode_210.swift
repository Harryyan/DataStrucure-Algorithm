/*
 There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
 You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

 For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
 Return the ordering of courses you should take to finish all courses. If there are many valid answers,
 return any of them. If it is impossible to finish all courses, return an empty array.
 */
import Foundation

final class Solution_210 {
    
    // tc: O(V*E)
    // sc: O(V*E)
    // took me 25 mins from reading to 1st AC
    func findOrder(_ numCourses: Int, _ prerequisites: [[Int]]) -> [Int] {
        var indegree = Counter().inDegree(prerequisites)    // what courses I need to learn
        let outdegree = Counter().outDegree(prerequisites)  // what courses need me
        
        var queue: [Int] = []   // better to use Deque, but this is not built-in DS
        var result = [Int]()
        
        // get courses which has no dependencies
        for i in 0..<numCourses {
            if indegree[i] == nil {
                queue.append(i)
            }
        }
        
        var coursesCanTake = queue.count
        
        // find circle. return []
        if coursesCanTake == 0 {
            return []
        }
        
        // BFS
        while queue.count > 0 {
            let index = queue.removeLast()
            result.append(index)
            let outs = outdegree[index]
            
            // udpate queue when course available
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
        
        if result.count == numCourses {
            return result
        } else {
            return []
        }
    }
}
