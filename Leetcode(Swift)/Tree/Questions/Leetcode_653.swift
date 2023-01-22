/*
 Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.
 */

import Foundation

final class Solution_653 {
    
    var nums: [Int] = []
    
    func findTarget(_ root: TreeNode?, _ k: Int) -> Bool {
        inOrder(root)
        
        var left = 0
        var right = nums.count - 1
        
        while left < right {
            if nums[left] + nums[right] > k {
                right -= 1
            } else if nums[left] + nums[right] < k {
                left += 1
            } else {
                return true
            }
        }
        
        return false
    }
    
    private func inOrder(_ node: TreeNode?) {
        if let node = node {
            inOrder(node.left)
            nums.append(node.val)
            inOrder(node.right)
        }
    }
}
