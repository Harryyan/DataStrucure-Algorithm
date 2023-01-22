import Foundation

class Solution_222 {
    // BFS
    func countNodes(_ root: TreeNode?) -> Int {
        guard let root = root else { return 0 }
        
        var queue: [TreeNode] = []
        queue.append(root)
        var level = 0
        var index = 0
        var perfect = false
        var flag = false
        var vv = 1
        
        while !queue.isEmpty {
            var temp: [TreeNode] = []
            level += 1
            
            if flag {
                break
            }
            
            for (i, item) in queue.enumerated() {
                let left = item.left
                let right = item.right
                
                if left != nil && right == nil {
                    index = i
                    flag = true
                    if temp.count == 0 {
                        temp.append(left!)
                    }
                    break
                }
                
                if left == nil && i == 0 {
                    perfect = true
                    flag = true
                    break
                }
                
                if left == nil && i > 0 {
                    flag = true
                    vv = 0
                    index = i
                    break
                }
                
                if left != nil {
                    temp.append(left!)
                }
                
                if right != nil {
                    temp.append(right!)
                }
            }
            
            queue = temp
        }
        
        var res = 0
        if perfect {
            let a = pow(2,level).intValue-1
            res = a
        } else {
            let a = pow(2,level-1).intValue - 1 + 2*index+vv
            res = a
        }
        
        return res
    }
}

class Solution_222_DFS {
    // DFS
    // O(logN * logN)
    func countNodes(_ root: TreeNode?) -> Int {
        guard let root = root else { return 0 }
        
        let leftLevel = countLevels(root.left)
        let rightLevel = countLevels(root.right)
        
        // 左边是满二叉树
        if leftLevel == rightLevel {
            return countNodes(root.right) + pow(2, leftLevel).intValue
        } else {
            // 右边是满二叉树
            return countNodes(root.left) + pow(2, rightLevel).intValue
        }
    }
    
    
    private func countLevels(_ node: TreeNode?) -> Int {
        var level = 0
        
        var node = node
        
        while node != nil {
            node = node?.left
            level += 1
        }
        
        return level
    }
}
