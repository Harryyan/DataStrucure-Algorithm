import Foundation

// 创建一个二维数组 dp[len][len]
// dp[i][j]: i~j 组成的字数组 亚历克斯能够赢得的分数
// dp[i][j]: 这是有2个选择: 求出最大值
// 1: 亚历克斯拿走左边的i, 剩下dp[i+1][j] 就是李能够获取的最大分数, = piles[i] - dp[i+1][j]
// 2: 亚历克斯拿走右边的j, 剩下dp[i][j-1] 就是李能够获取的最大分数, = piles[j] - dp[i][j-1]
// 特例dp[i][i] 意味着只有一堆，那么肯定赢，= piles[i]

final class Solution_877_V1 {
    func stoneGame(_ piles: [Int]) -> Bool {
        if piles.count <= 2 {
            return true
        }

        var dp = Array(repeating: Array(repeating: 0, count: piles.count), count: piles.count)
        
        for i in 0..<piles.count {
            dp[i][i] = piles[i]
        }
        
        for i in 0..<piles.count-1 {
            let index = piles.count-2-i
            
            for j in index+1..<piles.count {
                // 状态方程:
                // dp存储的是先手和后手获取石子的差异
                // 无论奇数，还是偶数堆，状态方程不变
                // 我们只需要使用当前先手堆石子个数减去之前先手差异，若>0, 则可获胜
                dp[index][j] = max(piles[index] - dp[index+1][j], piles[j] - dp[index][j-1])
            }
        }
        
        return dp[0][piles.count - 1] > 0
    }
}
