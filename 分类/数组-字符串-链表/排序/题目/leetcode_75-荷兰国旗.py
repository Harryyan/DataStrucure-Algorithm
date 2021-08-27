from typing import List

# 给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
# 此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()


# 快速排序变种: 三向切分快速排序， 适用于有大量重复元素的数组
# 平均时间复杂度： N ~ NlogN

class Solution_3:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cursor = 0
        left = -1
        right= len(nums)

        while cursor < right:
            if nums[cursor] == 2:
                left += 1
                nums[cursor], nums[left] = nums[left], nums[cursor]
                cursor += 1
            elif nums[cursor] == 0:
                right -= 1
                nums[cursor], nums[right] = nums[right], nums[cursor]
            else:
                cursor += 1

        print(nums)

colors = [2,0,2,1,1,0]

s = Solution_3()
s.sortColors(colors)