from typing import List

# 给定一个未排序的整数数组，找到最长递增子序列的个数。

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 1

        dp = [1] * n
        count = [1] * n
        max_length = 0
        
        
#       对于每一个数nums[i]，看在它之前的数nums[j](0<= j < i)是否比当前数nums[i]小，如果nums[i] > nums[j]，那么相当于到nums[j]为止的最长递增子序列长度到nums[i]增加了1，
#       到nums[i]为止的最长递增子序列长度就变成了dp[i] = dp[j] + 1；但是因为满足nums[i] > nums[j] 的nums[j]不止一个，dp[i]应该取这些dp[j] + 1的最大值，并且这些dp[j] + 1
#       还会有相等的情况，一旦相等，到nums[i]为止的最长递增子序列个数就应该增加了。因此，具体的状态转移如下，在nums[i] > nums[j]的大前提下：
#       
#       如果dp[j] + 1 > dp[i]，说明最长递增子序列的长度增加了，dp[i] = dp[j] + 1，长度增加，数量不变 count[i] = count[j]
#       如果dp[j] + 1 == dp[i]，说明最长递增子序列的长度并没有增加，但是出现了长度一样的情况，数量增加 count[i] += count[j]
        
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                        
                    elif dp[j] + 1 == dp[i]:
                        count[i] += count[j]
                        
            max_length = max(max_length, dp[i])

        res = 0
        print(count)
        for i in range(n):
            if dp[i] == max_length:
                res += count[i]
                
        return res
    
n = [1,2,3,3,4]
s = Solution()

r = s.findNumberOfLIS(n)

print(r)