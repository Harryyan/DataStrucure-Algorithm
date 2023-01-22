# 给你一个整数数组 nums ，设计算法来打乱一个没有重复元素的数组。

# 实现 Solution class:

# Solution(int[] nums) 使用整数数组 nums 初始化对象
# int[] reset() 重设数组到它的初始状态并返回
# int[] shuffle() 返回数组随机打乱后的结果
#  
import random

class Solution:
    def __init__(self, nums):
        self.array = nums
        
        # deep copy
        self.original = list(nums)

    def reset(self):
        self.array = self.original
        self.original = list(self.original)
        return self.array

    def shuffle(self):
        for i in range(len(self.array)):
            swap_idx = random.randrange(i, len(self.array))
            self.array[i], self.array[swap_idx] = self.array[swap_idx], self.array[i]
        return self.array
    
