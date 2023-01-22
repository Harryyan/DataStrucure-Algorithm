/*
 A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them.
 A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
 The path sum of a path is the sum of the node's values in the path.
 Given the root of a binary tree, return the maximum path sum of any non-empty path.ßå
 */

import Foundation

final class Solution_124 {
    var result = -1001
    
    func maxPathSum(_ root: TreeNode?) -> Int {
        guard let root = root else { return 0 }
        
        _ = dfs(root)
        
        return result
    }
    
    private func dfs(_ node: TreeNode?) -> Int {
        guard let node = node else { return 0 }
        
        let left = dfs(node.left)
        let right = dfs(node.right)
        let tempResult = max(node.val, node.val + max(left, right))
        
        result = max(result, max(tempResult, left+right+node.val))
        
        return tempResult
    }
}
