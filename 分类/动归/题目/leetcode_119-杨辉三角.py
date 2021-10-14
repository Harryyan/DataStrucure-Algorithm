from typing import List

# 给定一个非负索引 rowIndex，返回「杨辉三角」的第 rowIndex 行。
# 在「杨辉三角」中，每个数是它左上方和右上方的数的和。

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [[1]]
        num = rowIndex + 1

        while len(res) < num:
            newRow = [a+b for a, b in zip([0]+res[-1], res[-1]+[0])]
            res.append(newRow)  

        return res[-1]


rowIndex = 5
s = Solution()
r = s.getRow(rowIndex)

print(r)