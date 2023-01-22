/*
 Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
 */
import Foundation


final class Solution_102 {
    
    func levelOrder(_ root: TreeNode?) -> [[Int]] {
        guard let root = root else { return [] }
        
        var queue = [TreeNode]()
        var result: [[Int]] = []
        
        queue.append(root)
        
        while queue.count > 0 {
            var values: [Int] = []
            var nextLevel = [TreeNode]()
            
            for q in queue {
                values.append(q.val)
                
                if let left = q.left {
                    nextLevel.append(left)
                }
                
                if let right = q.right {
                    nextLevel.append(right)
                }
            }
            
            queue = nextLevel
            result.append(values)
        }
        
        return result
    }
}
