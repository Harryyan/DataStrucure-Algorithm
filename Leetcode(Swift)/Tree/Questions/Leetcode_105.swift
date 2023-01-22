/*
 Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree
 and inorder is the inorder traversal of the same tree, construct and return the binary tree.
 
 */
import Foundation

final class Solution_105 {
    
    func buildTree(_ preorder: [Int], _ inorder: [Int]) -> TreeNode? {
        return dfs(preorder: preorder, p_start: 0, p_end: preorder.count, inorder: inorder, i_start: 0, i_end: inorder.count)
    }
    
    private func dfs(preorder: [Int], p_start: Int, p_end: Int, inorder: [Int], i_start: Int, i_end: Int) -> TreeNode? {
        guard p_start != p_end else { return nil }
        
        let newRootValue = preorder[p_start]
        let root = TreeNode(newRootValue)
        
        var i_root_index = 0
        
        for (index, value) in inorder.enumerated() {
            if newRootValue == value {
                i_root_index = index
                break
            }
        }
        
        let leftNum = i_root_index - i_start
        
        let left = dfs(preorder: preorder, p_start: p_start+1, p_end: p_start+leftNum+1, inorder: inorder, i_start: i_start, i_end: i_root_index)
        let right = dfs(preorder: preorder, p_start: p_start+leftNum+1, p_end: p_end, inorder: inorder, i_start: i_root_index + 1, i_end: i_end)
        
        root.left = left
        root.right = right
        
        return root
    }
}

class Solution_105_SubItems {
    func buildTree(_ preorder: [Int], _ inorder: [Int]) -> TreeNode? {
        return dfs(preorder: preorder, inorder: inorder,right: preorder.count)
    }
    
    private func dfs(preorder: [Int], inorder: [Int], right: Int) -> TreeNode? {
        guard preorder.count > 0 else { return nil }
        guard preorder.count > 1 else { return TreeNode(preorder[0]) }
        
        let root = preorder[0]
        let rootPostion = inorder.firstIndex(where: {$0==root})!
        
        let newPreLenLeft = rootPostion
        var newPreLeft: [Int] = []
        
        if newPreLenLeft > 0 {
            newPreLeft = Array(preorder[1...newPreLenLeft])
        }
        
        let newPreLenRight = right-1-rootPostion
        let newPreRight:[Int] = Array(preorder[1+newPreLenLeft..<right])
        
        let newInLeft:[Int] = Array(inorder[0...newPreLenLeft])
        var newInRight: [Int] = []
        
        if rootPostion+1 < inorder.count {
            newInRight = Array(inorder[(rootPostion+1)..<right])
        }
        
        let leftNode = dfs(preorder: newPreLeft, inorder: newInLeft, right: newPreLenLeft)
        let rightNode = dfs(preorder: newPreRight, inorder: newInRight,right: newPreLenRight)
        
        let node = TreeNode(root)
        node.left = leftNode
        node.right = rightNode
        
        return node
    }
    
}
