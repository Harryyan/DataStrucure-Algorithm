from typing import List

# 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

class Solution:
    
    def exist(self, board, word):
        row, col = len(board), len(board[0])

        def dfs(x, y, index):
            if board[x][y] != word[index]:
                return False
            if index == len(word) - 1:
                return True
            board[x][y] = '#'
            
            for choice in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                nx, ny = x + choice[0], y + choice[1]
                if 0 <= nx < row and 0 <= ny < col and dfs(nx, ny, index + 1):
                    return True
                
            board[x][y] = word[index]

        for i in range(row):
            for j in range(col):
                if dfs(i, j, 0):
                    return True
        return False
    
    
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"

s = Solution()
r = s.exist(board, word)


print(r)