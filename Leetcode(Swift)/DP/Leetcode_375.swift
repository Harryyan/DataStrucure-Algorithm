import Foundation

// We are playing the Guessing Game. The game will work as follows:
//
// I pick a number between 1 and n.
// You guess a number.
// If you guess the right number, you win the game.
// If you guess the wrong number, then I will tell you whether the number I picked is higher or lower, and you will continue guessing.
// Every time you guess a wrong number x, you will pay x dollars. If you run out of money, you lose the game.
// Given a particular n, return the minimum amount of money you need to guarantee a win regardless of what number I pick.

class Solution_375 {
    // 区间DP
    // 动归方程: dp[start][end] = min(dp[start][end], k + max(f[start][k-1], f[k+1][end]))
    func getMoneyAmount(_ n: Int) -> Int {
        // 初始化dp二维数组
        var dp: [[Int]] = Array(repeating: Array(repeating: Int.max, count: n+1), count: n+1)
        
        return f(1, n, &dp)
    }
    
    private func f(_ start: Int, _ end: Int, _ cache: inout [[Int]]) -> Int {
        if start >= end {
            return 0
        }
        
        // 若无缓存再计算
        if cache[start][end] == Int.max {
            for k in start...end {
                // 核心区间动态规划方程
                cache[start][end] = min(cache[start][end], k + max(f(start, k-1, &cache), f(k+1, end, &cache)))
            }
        }
        
        // 直接加载缓存
        return cache[start][end]
    }
}
