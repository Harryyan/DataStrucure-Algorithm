import Foundation

/*
 You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi]
 indicates that there is an undirected edge between nodes ai and bi in the graph.
 
 Return true if the edges of the given graph make up a valid tree, and false otherwise.
 */

final class Solution_261 {
    
    func validTree(_ n: Int, _ edges: [[Int]]) -> Bool {
        let unionFind = UnionFind(n: n)
        var set: Set<Int> = Set<Int>()
        
        for edge in edges {
            let a = edge[0]
            let b = edge[1]
            
            if unionFind.isConnected(a: a, b: b) {
                return false
            }
            
            unionFind.union(a: a, b: b)
        }
        
        for key in unionFind.dict.keys {
            set.insert(unionFind.find(key))
        }
        
        return set.count == 1
    }
}
