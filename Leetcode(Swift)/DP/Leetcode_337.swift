//
//  Leetcode_337.swift
//  Leetcode
//
//  Created by Harry on 24/03/22.
//

import Foundation

class Solution_337 {
    func rob(_ root: TreeNode?) -> Int {
        let result = dfs(root)

        return max(result[0], result[1])
    }

    private func dfs(_ node: TreeNode?) -> [Int] {
        guard let node = node else { return [0,0] }

        let left = dfs(node.left)
        let right = dfs(node.right)

        let val1 = max(left[1],left[0]) + max(right[0],right[1])            // not rob current node
        let val2 = node.val + left[0] + right[0]                            // rob current node

        return [val1, val2]
    }
}
