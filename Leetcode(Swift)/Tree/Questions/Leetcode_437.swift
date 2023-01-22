import Foundation

class Solution_437_Recursion {
    // tc: O(n^2)
    // sc: O(n)
    // time: 9 mins
    func pathSum(_ root: TreeNode?, _ targetSum: Int) -> Int {
        guard root != nil else { return 0 }
        
        return pathRootSum(root, targetSum) + pathSum(root!.left, targetSum) + pathSum(root!.right, targetSum)
    }

    private func pathRootSum(_ root: TreeNode?, _ target: Int) -> Int {
        guard root != nil else { return 0 }
        
        var count = 0
        
        if root!.val == target {
            count += 1
        }

        let left = pathRootSum(root!.left, target - root!.val)
        let right = pathRootSum(root!.right, target - root!.val)
    
        count += left + right
        
        return count
    }
}

// pre sum
class Solution_437_Recursion_Best {
    var preSum: [Int:Int] = [:]   // record different pre sum number
    var pre = 0
    var ans = 0
    
    func pathSum(_ root: TreeNode?, _ targetSum: Int) -> Int {
        preSum[0] = 1
        
        dfs(root, targetSum)
        
        return ans
    }
    
    private func dfs(_ node: TreeNode?, _ target: Int) {
        guard let node = node else { return }
        
        pre += node.val
        
        if let value = preSum[pre-target] {
            ans += value
        }
        
        if let _ = preSum[pre] {
            preSum[pre]! += 1
        } else {
            preSum[pre] = 1
        }
        
        dfs(node.left, target)
        dfs(node.right, target)
        
        if let _ = preSum[pre] {
            preSum[pre]! -= 1
        } else {
            preSum[pre] = 0
        }
        
        pre -= node.val
    }
}
