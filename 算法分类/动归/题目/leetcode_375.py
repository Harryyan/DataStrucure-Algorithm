# We are playing the Guessing Game. The game will work as follows:

# I pick a number between 1 and n.
# You guess a number.
# If you guess the right number, you win the game.
# If you guess the wrong number, then I will tell you whether the number I picked is higher or lower, and you will continue guessing.
# Every time you guess a wrong number x, you will pay x dollars. If you run out of money, you lose the game.
# Given a particular n, return the minimum amount of money you need to guarantee a win regardless of what number I pick.

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        # dp[i][j] 猜中i-j用的最小钱
        dp = [[0 for j in range(n+1)] for i in range(n+1)]
        for d in range(1,n):
            for i in range(1,n+1):
                if i+d > n:
                    break
                min_cost = float('inf')
                for k in range(i,i+d+1):
                    cost = k + max(dp[i][k-1], (dp[k+1][i+d] if k+1<=i+d else 0))
                    min_cost = min(min_cost,cost)
                dp[i][i+d] = min_cost
                
        return dp[1][n]