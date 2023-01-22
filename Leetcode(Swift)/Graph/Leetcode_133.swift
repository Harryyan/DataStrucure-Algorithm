import Foundation

class Solution_133 {
    class Node {
        public var val: Int
        public var neighbors: [Node?]
        public init(_ val: Int) {
            self.val = val
            self.neighbors = []
        }
    }
    
    // tc: O(VE)
    // sc: O(V)
    // time: 6 mins
    func cloneGraph(_ node: Node?) -> Node? {
        guard let node = node else { return nil }
        
        var queue: [Node] = []
        var newQueue: [Node] = []
        let newSource = Node(node.val)
        var visited: [Node] = []
        
        queue.append(node)
        newQueue.append(newSource)
        visited.append(newSource)

        while !queue.isEmpty {
            let oldNode = queue.removeLast()
            let neibs = oldNode.neighbors
            
            let newNode = newQueue.removeLast()
            
            for nei in neibs {
                let node = visited.first(where: {$0.val == nei?.val })
                
                if node == nil {
                    let newNeiNode = Node(nei!.val)
                    newNode.neighbors.append(newNeiNode)
                    
                    queue.append(nei!)
                    newQueue.append(newNeiNode)
                    visited.append(newNeiNode)
                } else {
                    newNode.neighbors.append(node)
                }
            }
        }
        
        return newSource
    }
}
