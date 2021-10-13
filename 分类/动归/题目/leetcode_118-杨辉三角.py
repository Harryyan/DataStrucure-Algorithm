from typing import List

# 给定一个非负整数 numRows，生成「杨辉三角」的前 numRows行,
# 在「杨辉三角」中，每个数是它左上方和右上方的数的和


class Solution:
    # 时间复杂度: O(n²)
    # 空间复杂度: O(1)
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0: return []
        res = [[1]]

        while len(res) < numRows:
            newRow = [a+b for a, b in zip([0]+res[-1], res[-1]+[0])]
            res.append(newRow)  

        return res

numRows = 18
s = Solution()

print(s.generate(numRows))