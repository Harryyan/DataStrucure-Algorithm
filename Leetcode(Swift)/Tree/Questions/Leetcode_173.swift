import Foundation

/*
 Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):
 
 BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
 boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
 int next() Moves the pointer to the right, then returns the number at the pointer.
 Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.
 
 You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.
 */

final class BSTIterator {
    private var elements: [Int] = []
    private var index = -1
    private var totalCount = 0
    
    init(_ root: TreeNode?) {
        inOrderTraversal(root)
        
        totalCount = elements.count
    }
    
    func next() -> Int {
        index += 1
        
        guard index < totalCount else { return -1 }
        
        return elements[index]
    }
    
    func hasNext() -> Bool {
        let nextIndex = index + 1
        
        return nextIndex < totalCount
    }
    
    private func inOrderTraversal(_ node: TreeNode?) {
        guard let node = node else { return }
        
        let _ = inOrderTraversal(node.left)
        
        elements.append(node.val)
        
        let _ = inOrderTraversal(node.right)
    }
}

// 单调栈
// 构造迭代器
final class BSTIterator_Opt {
    private var stack: [TreeNode?] = []
    
    init(_ root: TreeNode?) {
        var node = root
        
        // 讲左节点入栈
        while node != nil {
            stack.append(node)
            node = node?.left
        }
    }
    
    func next() -> Int {
        let currentNode: TreeNode? = stack.removeLast()
        var node = currentNode?.right
        
        while node != nil {
            stack.append(node)
            node = node?.left
        }
        
        return currentNode?.val ?? -1
    }
    
    func hasNext() -> Bool {
        return stack.count > 0
    }
}
