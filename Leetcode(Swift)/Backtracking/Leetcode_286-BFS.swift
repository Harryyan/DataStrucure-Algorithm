import Foundation
import Collections

/*
 You are given an m x n grid rooms initialized with these three possible values.
 
 -1 A wall or an obstacle.
 0 A gate.
 INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
 Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.
 */

final class Solution_286 {
    func wallsAndGates(_ rooms: inout [[Int]]) {
        let INF = 2147483647
        let rows = rooms.count
        
        guard rows > 0 else { return }
        
        let cols = rooms[0].count
        
        var queue: Deque<(Int, Int, Int)> = []
        let neibours = [(0,1),(1,0),(0,-1),(-1,0)]
        
        for row in 0..<rows {
            for col in 0..<cols {
                if rooms[row][col] == 0 {
                    queue.append((row, col, 0))
                }
            }
        }
        
        while queue.count > 0 {
            let (r, c, dist) = queue.popFirst()!
            
            for (row, col) in neibours {
                let nr = r + row
                let nc = c + col
                
                if 0 <= nr && nr < rows && 0 <= nc && nc < cols && rooms[nr][nc] == INF {
                    rooms[nr][nc] = dist + 1
                    queue.append( (nr, nc, dist + 1) )
                }
            }
        }
    }
}
