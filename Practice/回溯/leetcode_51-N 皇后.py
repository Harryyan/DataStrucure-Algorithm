
# n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

# 给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。

# 每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

from typing import Collection, List

class Solution:
    result = []
    result2 = []
    
    def callNQueens(self, row, n):
        if row == n:
            self.printNQueens(n)
            return;
        
        for col in range(n):
            if self.isOK(row, col, n):
                self.result[row] = col
                self.callNQueens(row+1,n)

    def isOK(self, row, column, n) -> bool:
        leftUp = column - 1
        rightUp = column + 1
        
        for i in range(row-1, -1, -1):
            if self.result[i] == column: return False
            if leftUp >= 0 and self.result[i] == leftUp: return False
            if rightUp < n and self.result[i] == rightUp: return False
                
            leftUp -= 1
            rightUp += 1
        
        return True
    
    def printNQueens(self, n):
        s = []
        
        for i in range(n):
            r = ""
            for j in range(n):
                if self.result[i] == j: r += "Q"; #print("Q", end="\t")
                else: r += "."; #print(".", end="\t")
            s.append(r)
            #print("\n")
        #print(s) 
        self.result2.append(s)  
        #print("\n")
        
        
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1: return [["Q"]]
        
        self.result = ["."] * n
        self.callNQueens(0, n)
        
        return self.result2
        
        
s = Solution()
r = s.solveNQueens(2)

print(r)