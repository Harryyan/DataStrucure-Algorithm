import Foundation

class Solution_1504 {
    // tc: O(m²n²)
    // sc: O(1)
    // time: 23 mins
    // BF
    // 可用单调栈减少遍历层数
    func numSubmat(_ mat: [[Int]]) -> Int {
        let rows = mat.count
        let cols = mat[0].count
        var result = 0
        var left = 0
        var top = 0
        var height = Int.max

        for i in 0..<rows {
            for j in 0..<cols {
                left = j
                height = Int.max

                // 向左回溯
                while left >= 0 {
                    top = i

                    // 向上回溯
                    while top >= 0 && i - top < height && mat[top][left] > 0 {
                        result += 1
                        top -= 1
                    }

                    // 计算右侧一列和当前列是否可以构成矩形，所以这里要记录下右侧1的高度
                    height = min(height, i - top)
                    left -= 1
                }
            }
        }

        return result
    }
}
