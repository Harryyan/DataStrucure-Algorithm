from typing import List

# Given an unsorted integer array nums, return the smallest missing positive integer.
# You must implement an algorithm that runs in O(n) time and uses constant extra space.


# 下面我们通过三次遍历找到缺失的第一个正数，感觉这样比较好理解
# 遍历：小于等于0 和 大于等于n+1 的数字一律改为 n+1 不改变最后结果 且此时所有元素在 1～n+1 之间
# 遍历：遇到 1<|num|<n 之间的数字 便令第|num|个数字变成负的 (如果之前是正的 变成负的 否则不变)
# 再次遍历：如果第i个数字是正的 则说明之前没有出现过i 如果所有数字是负的 则说明1～n都出现了 返回n+1

# 缺失的数套路：
# 元素范围 1 ~ n+1
# 利用index，未排序可以使用 value变负index的方法

class Solution:
    # tc: O(n)
    # sc: O(1)
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i]>=n+1 or nums[i]<=0: nums[i]=n+1
        for i in range(n):
            num=nums[i]
            if 1<=abs(num)<=n and nums[abs(num)-1]>0:
                nums[abs(num)-1]=-nums[abs(num)-1] 

        print(nums)
        for i in range(n):
            if nums[i]>0: return i+1
        return n+1


nums = [1,4,3,-2,6,7,8]
s = Solution()

r = s.firstMissingPositive(nums)

print(r)