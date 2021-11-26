# 给定一个非负整数数组，你最初位于数组的第一个位置。
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 你的目标是使用最少的跳跃次数到达数组的最后一个位置。

# 假设你总是可以到达数组的最后一个位置。

from typing import DefaultDict, List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        maxPos = start = end = step = 0
        while end < n - 1 :
            # end >= n-1时，已可以到达终点
            while start <= end :
                maxPos = max(maxPos , start + nums[start])
                start += 1
            # 查找最远的可达点
            print(maxPos)
            end = maxPos
            step += 1
            # 准备下一次跳跃，次数加一
        return step

    
s = Solution()
nums = [4,1,1,3,1,1,1,2]
result = s.jump(nums)
print(result)