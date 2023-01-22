import Foundation


class Solution_785 {
    var states: [Int: Int] = [:]
    var result = true
    
    func isBipartite(_ graph: [[Int]]) -> Bool {
        let len = graph.count
        
        for i in 0..<len {
            states[i] = 0
        }
        
        for i in 0..<len {
            if states[i] == 0 {
                dfs(i, 1, graph)
                if !result {
                    break
                }
            }
        }
        
        return result
    }
    
    private func dfs(_ i: Int, _ state: Int, _ graph: [[Int]]) {
        let neis = graph[i]
        states[i] = state
        
        for nei in neis {
            if states[nei] == 0 {
                dfs(nei, state == 1 ? 2 : 1, graph)
                if !result {
                    return
                }
            } else if states[nei] == state  {
                result = false
                return
            }
        }
    }
}
