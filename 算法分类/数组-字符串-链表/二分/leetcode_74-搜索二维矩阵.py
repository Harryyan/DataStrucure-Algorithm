from typing import List

# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
# 每行中的整数从左到右按升序排列。
# 每行的第一个整数大于前一行的最后一个整数。


class Solution:
    def binary_Search(self, items, start, end, target):
        if start >= end:
            if items[end] == target:
                return True
            else:
                return False

        mid = start + ((end - start) >> 1)

        if target <= items[mid]:
            return self.binary_Search(items, start, mid, target)
        else:
            return self.binary_Search(items, mid + 1, end, target)
        
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target > matrix[-1][-1] or target < matrix[0][0]: return False
        
        result = False
        
        for interval in matrix:
            if interval[0] < target < interval[-1]:
                result = self.binary_Search(interval, 0, len(interval)-1,target)
                break
            
            if target == interval[0] or target == interval[-1]: result = True; break
            
        return result
    
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

s = Solution()
r = s.searchMatrix(matrix,target)

print(r)