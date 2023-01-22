from typing import List

# 给定一个非负索引 rowIndex，返回「杨辉三角」的第 rowIndex 行。
# 在「杨辉三角」中，每个数是它左上方和右上方的数的和。


# leetcode 119
class Solution:
    # 时间复杂度: O(rowIndex²)
    # 空间复杂度: O(rowIndex²)
    def getRow(self, rowIndex: int) -> List[int]:
        res = [[1]]
        num = rowIndex + 1

        while len(res) < num:
            newRow = [a+b for a, b in zip([0]+res[-1], res[-1]+[0])]
            res.append(newRow)  

        return res[-1]

class Solution_ACE:
    # 时间复杂度: O(rowIndex²)
    # 空间复杂度: O(rowIndex)

    # 该变体亮点在于优化了时间复杂度，使用一维数组一步一步构造结果，
    # 符合动态规划多阶段决策最优解模型

    def getRow(self, rowIndex: int) -> List[int]:
        res = [1] * (rowIndex + 1)

        for i in range(2, rowIndex + 1):
            for j in range(i - 1, 0, -1):
                res[j] += res[j - 1]
        return res


rowIndex = 5
s = Solution()
r = s.getRow(rowIndex)

print(r)