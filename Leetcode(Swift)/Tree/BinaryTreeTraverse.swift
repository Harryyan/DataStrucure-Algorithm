import Foundation

class Inorder {
    var result: [Int] = []
    
    func inorderTraversal(_ root: TreeNode?) -> [Int] {
        inorder(root)
        
        return result
    }
    
    func inorder(_ node: TreeNode?) {
        guard let node = node else { return }
        
        inorder(node.left)
        result.append(node.val)
        inorder(node.right)
    }
    
    
    func inorderStack(_ root: TreeNode?) -> [Int] {
        var res: [Int] = []
        var root_cp = root
        var queue: [TreeNode] = []
        
        while root_cp != nil || !queue.isEmpty {
            while root_cp != nil {
                queue.append(root_cp!)
                root_cp = root_cp?.left
            }
            
            let node = queue.removeLast()
            res.append(node.val)
            root_cp = node.right
        }
        
        return res
    }
}


class Preorder {
    var result: [Int] = []
    
    func preorderTraversal(_ root: TreeNode?) -> [Int] {
        preorder(root)
        
        return result
    }
    
    func preorder(_ node: TreeNode?) {
        guard let node = node else { return }
        
        result.append(node.val)
        preorder(node.left)
        preorder(node.right)
    }
    
    
    func preorderStack(_ root: TreeNode?) -> [Int] {
        var res: [Int] = []
        var root_cp = root
        var queue: [TreeNode] = []
        
        while root_cp != nil || !queue.isEmpty {
            while root_cp != nil {
                res.append(root_cp!.val)
                queue.append(root_cp!)
                root_cp = root_cp?.left
            }
            
            let node = queue.removeLast()
            root_cp = node.right
        }
        
        return res
    }
}

class NaryTree {
    class Node {
        public var val: Int
        public var children: [Node]
        public init(_ val: Int) {
            self.val = val
            self.children = []
        }
    }
    
    var res: [Int] = []
    func postorder(_ root: Node?) -> [Int] {
        guard let root = root else { return [] }
        
        post(root)
        
        return res
    }
    
    func post(_ node: Node?) {
        guard node != nil else { return }
        
        for child in node!.children {
            post(child)
        }
        
        res.append(node!.val)
    }
    
    func postUsingStack(_ node: Node?) -> [Int] {
        guard let root = node else { return [] }
        
        var stack: [Node] = [root]
        var res: [Int] = []
        
        while !stack.isEmpty {
            let node = stack.removeLast()
            
            res.append(node.val)
            
            for n in node.children {
                stack.append(n)
            }
        }
        
        return res.reversed()
    }
}
