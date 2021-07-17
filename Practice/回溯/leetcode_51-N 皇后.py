
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
        
        # 每次计算浪费时间，可以提前计算
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

# 该方法高效的原因是： 使用左对角，右对角来标明哪些位置已经不能占据
class Solution_Advanced:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = [] # 记录结果
        col, diagr, diagl, board = [True]*n, [True]*(2*n-1), [True]*(2*n-1), [['.' for _ in range(n)] for _ in range(n)]
        # col, diagr, diagl 的元素分别表示当前列、右对角线、左对角线是否还可以放置；board为记录摆放位置的n*n矩阵
        def traceback(i, j):
            if i >= n: return # 当前行超过最大行号，返回
            if not col[j] or not diagr[j-i+n-1] or not diagl[j+i]: return # 当前列或右对角线或左对角线不能放置皇后，返回
            board[i][j] = 'Q' # 当前位置可以放置，将board对应位置的元素赋为'Q'
            if i == n - 1 and col[j] and diagr[j-i+n-1] and diagl[j+i]: # 当前已到最后一行，且当前位置可以放置，将摆放结果按正确的形式加入res中
                res.append([''.join(line) for line in board])
            # 此后说明，当前位置可放置且未到最后一行
            col[j], diagr[j-i+n-1], diagl[j+i] = False, False, False # 将当前位置对应的列、左右对角线的记为不能放置，并继续下一行的遍历
            for k in range(n):
                traceback(i+1, k)
            col[j], diagr[j-i+n-1], diagl[j+i], board[i][j] = True, True, True, '.' # 恢复当前位置的各参数，回溯（关键！）
        for j in range(n): # 从首行开始，遍历每一列
            traceback(0, j)
        return res # 返回结果
        
        
s = Solution()
r = s.solveNQueens(2)

print(r)