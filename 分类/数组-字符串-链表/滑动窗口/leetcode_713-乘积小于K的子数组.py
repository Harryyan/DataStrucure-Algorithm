
# 给定一个正整数数组 nums和整数 k 。

# 请找出该数组内乘积小于 k 的连续的子数组的个数。

# 遍历求前追乘积，然后取区间


class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        ret, left, total = 0, 0, 1
        for i, j in enumerate(nums):
            total *= j
            while left <= i and total >= k:
                total //= nums[left]
                left += 1
            ret += i - left + 1
        
        return ret
    
    
s = Solution()
nums = [10,5,2,6]
k = 100

print(s.numSubarrayProductLessThanK(nums, k))