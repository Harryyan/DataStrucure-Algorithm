//
//  Leetcode_114.swift
//  Leetcode
//
//  Created by Harry on 21/02/22.
//

import Foundation

class Solution_114_Recursion {
    func flatten(_ root: TreeNode?) {
        guard root != nil else { return }
        
        _ = dfs(root)
    }

    private func dfs(_ node: TreeNode?) -> TreeNode? {
        guard node != nil else { return nil }
        
        if node?.left == nil && node?.right == nil {
            return node
        }
        
        var left = dfs(node?.left)
        var right = dfs(node?.right)
        
        if let left = left {
            node?.right = left
            node?.left = nil
        }
        
        if let right = right {
            if left != nil {
                var node = left
                while node?.right != nil {
                    node = node?.right
                }
                
                node?.right = right
            }
        }
        
        return node
    }
}

// 寻找前驱结点
class Solution_114_Iteration {
    
    func flatten(_ root: TreeNode?) {
        guard root != nil else { return }
        
        var cur = root
        
        while cur != nil {
            if let left = cur?.left {
                let next = left
                var predecessor = next
                
                while predecessor.right != nil {
                    predecessor = predecessor.right!
                }
                
                predecessor.right = cur?.right
                cur?.left = nil
                cur?.right = next
            }
            
            cur = cur?.right
        }
    }
}
