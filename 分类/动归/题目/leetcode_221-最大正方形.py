from typing import List

# 在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。
# leetcode 221
import math

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        maxSum = 0

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[i][j] == 1:
                    if matrix[i - 1][j - 1] == 0 or matrix[i - 1][j] == 0 or matrix[i][j - 1] == 0:
                        matrix[i][j] = 1
                    else:
                        if matrix[i - 1][j - 1] > 1 and matrix[i - 1][j] > 1 and matrix[i][j - 1] > 1:
                            matrix[i][j] = pow(math.sqrt(matrix[i - 1][j - 1])+1, 2)
                        elif matrix[i - 1][j - 1] >= 1 and (matrix[i - 1][j] == 1 or matrix[i][j - 1] == 1):
                            matrix[i][j] = 4

                    maxSum = max(matrix[i][j], maxSum)
        return maxSum  

class Solution_Str:
    # 时间复杂度：O(mn)
    # 空间复杂度：O(mn)
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if(not matrix):
            return 0
        m=len(matrix)
        n=len(matrix[0])
        res=0
        dp=[[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if(matrix[i-1][j-1]=="1"):
                    dp[i][j]=min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
                    res=max(dp[i][j],res)
        return res*res   

matrix = [[0,0,0,0,0],[0,1,1,0,0],[0,1,1,1,0],[0,1,1,1,0],[0,0,0,0,0]]
s = Solution()

r = s.maximalSquare(matrix)
print(r)

print('1' + 3)