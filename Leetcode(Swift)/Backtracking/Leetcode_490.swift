import Foundation

class Solution_490 {

    /// Determines whether the ball could stop at the destination.
    ///
    /// - Parameters:
    ///   - maze: The maze.
    ///   - start: Start position of the ball.
    ///   - destination: Destination position.
    /// - Returns: True if the ball could stop at the destination, otherwise returns false.
    ///
    /// - Complexity:
    ///   - time: O(n * m), where n is the number of rows in the maze, and m is the number
    ///     of columns in the maze.
    ///   - space: O(n * m), where n is the number of rows in the maze, and m is the number
    ///     of columns in the maze.
    func hasPath(_ maze: [[Int]], _ start: [Int], _ destination: [Int]) -> Bool {
        let directions: [(x: Int, y: Int)] = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        var visited = [[Bool]](repeating: [Bool](repeating: false, count: maze[0].count), count: maze.count)
        var queue = [(x: Int, y: Int)]()
        let m = maze.count
        let n = maze[0].count
        let value = (m+n) * 2
        var distance: [[Int]] = Array(repeating: Array(repeating: value, count: n), count: m)
        distance[start[0]][start[1]] = 0
        queue.append((start[0], start[1]))

        let destination = (x: destination[0], y: destination[1])
        visited[start[0]][start[1]] = true
        
        while !queue.isEmpty {
            let curr = queue.removeFirst()

            guard curr.x != destination.x || curr.y != destination.y else {
                print(distance[destination.x][destination.y])
                return true
            }

            for direction in directions {
                var x = curr.x + direction.x
                var y = curr.y + direction.y
                var count = 0

                while x >= 0, y >= 0, x < maze.count, y < maze[x].count, maze[x][y] == 0 {
                    x += direction.x
                    y += direction.y
                    
                    count += 1
                }

                guard !visited[x - direction.x][y - direction.y] else { continue }
                
                if distance[curr.x][curr.y] + count < distance[x-direction.x][y-direction.y] {
                    distance[x-direction.x][y-direction.y] = distance[curr.x][curr.y] + count
                }
                
                queue.append((x - direction.x, y - direction.y))
                visited[x - direction.x][y - direction.y] = true
            }

        }

        return false
    }

}
