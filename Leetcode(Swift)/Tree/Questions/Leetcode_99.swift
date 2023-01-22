import Foundation

class Solution_99 {
    var stack: [Int] = []
    var first = -1
    var second = -1
    
    func recoverTree(_ root: TreeNode?) {
        inOrder(root)
        findTwoWrongNumbers()
        recover(root, 2)
    }
    
    private func inOrder(_ root: TreeNode?) {
        guard let root = root else { return }
        
        inOrder(root.left)
        stack.append(root.val)
        inOrder(root.right)
    }
    
    private func findTwoWrongNumbers() {
        var flag = false
        
        for i in 0..<stack.count-1 {
            if stack[i+1] < stack[i] {
                if !flag {
                    first = i
                    flag = true
                } else {
                    second = i+1
                }
            }
        }
        
        if second == -1 {
            second = first+1
        }
        
        first = stack[first]
        second = stack[second]
    }
    
    private func recover(_ node: TreeNode?, _ count: Int) {
        guard let node = node, count > 0 else { return }
        var cc = count
        
        if node.val == first || node.val == second {
            node.val = node.val == first ? second : first
            cc -= 1
        }
        
        recover(node.left, cc)
        recover(node.right, cc)
    }
}
