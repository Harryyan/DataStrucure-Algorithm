import Foundation

// 返回起始点到每个点的最短距离
final class Dijkstra {
    
    // 使用领接矩阵存储稠密图
    func startWith(start: Int, matrix: [[Int]]) -> [Int] {
//        var visited: [Int] = []
        var distance: [Int] = matrix[start]
        var nonVisited: [Int] = []
        
        // 初始化
        for i in 0..<matrix.count {
            if i != start {
                nonVisited.append(i)
            }
        }
        
        while nonVisited.count > 0 {
            var idx = nonVisited[0]
            
            // 找到未访问集合中的最小值索引
            for i in nonVisited {
                if distance[i] < distance[idx] {
                    idx = i
                }
            }
            
            // 更新集合
            nonVisited.remove(object: idx)
            
            // 计算新的距离
            for i in nonVisited {
                let dis = distance[i] + matrix[idx][i]
                
                distance[i] = min(distance[i], dis)
            }
        }
        
        return distance
    }
    
    
    
}
