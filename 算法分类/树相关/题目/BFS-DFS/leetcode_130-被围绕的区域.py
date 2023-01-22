# 给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' ，找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
# leetcode-130

class Solution:
    # 时间复杂度: O(mn)
    # 空间复杂度: O(1)
    def solve(self, board):
        row, col = len(board), len(board[0])

        def dfs(x, y):
            if board[x][y] != 'O':
                return
            else:
                 board[x][y] = '#'
            for c in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                if 0 <= x + c[0] < row and 0 <= y + c[1] < col:
                    dfs(x + c[0], y + c[1])

        # 遍历四条边界
        for i in range(row):
            dfs(i, 0)
            dfs(i, col - 1)
        for j in range(1, col - 1):
            dfs(0, j)
            dfs(row - 1, j)

        for i in range(row):
            for j in range(col):
                board[i][j] = 'O' if board[i][j] == '#' else 'X'
                

board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
s = Solution()

s.solve(board)

print(board)