import Foundation

// Given the root of a binary tree, return the sum of all left leaves.

class Solution_11 {
    
    var totalSum = 0
    
    func sumOfLeftLeaves(_ root: TreeNode?) -> Int {
        guard root != nil else { return 0 }
        
        sum(of: root)
        
        return totalSum
    }
    
    private func sum(of node: TreeNode?) {
        guard let node = node else { return }
        
        if let left = node.left,
           left.left == nil &&
            left.right == nil {
            totalSum += node.left?.val ?? 0
        }
        
        sum(of: node.left)
        sum(of: node.right)
    }
}
