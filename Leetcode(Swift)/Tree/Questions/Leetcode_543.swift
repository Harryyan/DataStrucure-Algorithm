/*
 Given the root of a binary tree, return the length of the diameter of the tree.
 
 The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
 
 The length of a path between two nodes is represented by the number of edges between them.
 
 */

import Foundation

final class Solution_543 {
    
    var result = 0
    
    func diameterOfBinaryTree(_ root: TreeNode?) -> Int {
        
        func height(node: TreeNode?) -> Int {
            guard let node = node else { return 0 }
            
            let l_m = height(node: node.left)
            let r_m = height(node: node.right)
            
            result = max(result, l_m + r_m)
            
            return 1 + max(l_m, r_m)
        }
        
        height(node: root)
        
        return self.result
    }
}
