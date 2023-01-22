import Foundation

class Solution_863 {
    // tc: O(n)
    // sc: O(n)
    // other solution: 构建领接表, 例如 {3:[5,1], 5: [3,6,2], ...}
    // 然后BFS
    var parents: [Int: TreeNode] = [:]
    var res: [Int] = []

    func distanceK(_ root: TreeNode?, _ target: TreeNode?, _ k: Int) -> [Int] {
        guard let root = root else { return [] }

        buildParent(root)
        findRes(target, nil, 0, k)

        return res
    }

    private func buildParent(_ node: TreeNode) {
        if node.left != nil {
            parents[node.left!.val] = node
            buildParent(node.left!)
        }

        if node.right != nil {
            parents[node.right!.val] = node
            buildParent(node.right!)
        }
    }

    private func findRes(_ node: TreeNode?, _ from: TreeNode?, _ depth: Int, _ k: Int) {
        guard let node = node else { return }

        if depth == k {
            res.append(node.val)
            return
        }

        // avoid loop the same side
        if node.left?.val != from?.val {
            findRes(node.left, node, depth+1, k)
        }

        if node.right?.val != from?.val {
            findRes(node.right, node, depth+1, k)
        }

        if parents[node.val]?.val != from?.val {
            findRes(parents[node.val], node, depth + 1, k);
        }
    }
}
