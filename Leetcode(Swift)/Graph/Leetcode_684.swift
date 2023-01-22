/*
 In this problem, a tree is an undirected graph that is connected and has no cycles.

 You are given a graph that started as a tree with n nodes labeled from 1 to n,
 with one additional edge added. The added edge has two different vertices chosen from 1 to n,
 and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi]
 indicates that there is an edge between nodes ai and bi in the graph.

 Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.
 */
import Foundation

final class Solution_684 {
    
    func findRedundantConnection(_ edges: [[Int]]) -> [Int] {
        let unionFind = UnionFind(n: edges.count + 1)   // value from 1
        
        for edge in edges {
            let a = edge[0]
            let b = edge[1]
            
            if unionFind.isConnected(a: a, b: b) {
                return edge
            }
            
            unionFind.union(a: a, b: b)
        }
        

        return []
    }
}
