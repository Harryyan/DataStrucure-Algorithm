import Foundation

/*
 Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
 According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined
 between two nodes p and q as the lowest node in T that has both p and q as descendants
 (where we allow a node to be a descendant of itself).”
 */

class Leetcode_236 {
    func lowestCommonAncestor(_ root: TreeNode?,
                              _ p: TreeNode?,
                              _ q: TreeNode?) -> TreeNode? {
        
        guard let root = root else { return nil }
        
        if root.val == p?.val || root.val == q?.val {
            return root
        }
        
        let left = lowestCommonAncestor(root.left, p, q)
        let right = lowestCommonAncestor(root.right, p, q)
        
        if left == nil {
            return right
        }
        
        if right == nil {
            return left
        }
        
        return root
    }
}
