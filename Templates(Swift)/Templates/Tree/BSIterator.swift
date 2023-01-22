import Foundation

final class BSTIterator {
    private var stack: [TreeNode?] = []
    private let forward: Bool
    private let invalidValue = ~0
    
    init(_ root: TreeNode?, _ forward: Bool) {
        let node = root
        self.forward = forward
        
        forward ? pushLeftNodes(of: node) : pushRightNodes(of: node)
    }
    
    func hasNext() -> Bool {
        return stack.count > 0
    }
    
    func next() -> Int {
        let node: TreeNode? = stack.removeLast()
        
        forward ? pushLeftNodes(of: node?.right) : pushRightNodes(of: node?.left)
        
        return node?.val ?? invalidValue
    }
    
    func pushLeftNodes(of root: TreeNode?) {
        var node: TreeNode? = root
        
        while node != nil {
            stack.append(node)
            node = node?.left
        }
    }
    
    func pushRightNodes(of root: TreeNode?) {
        var node: TreeNode? = root
        
        while node != nil {
            stack.append(node)
            node = node?.right
        }
    }
    
    func peek() -> Int {
        return stack.last??.val ?? invalidValue
    }
}

public class TreeNode {
    public var val: Int
    public var left: TreeNode?
    public var right: TreeNode?
    public init() { self.val = 0; self.left = nil; self.right = nil; }
    public init(_ val: Int) { self.val = val; self.left = nil; self.right = nil; }
    public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
        self.val = val
        self.left = left
        self.right = right
    }
}

