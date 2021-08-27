from typing import List

# 给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

# 此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        nums.sort()

        print(nums)


colors = [0]

s = Solution()
s.sortColors(colors)