from typing import List

# Given an integer array nums, return the maximum difference between two successive elements in its sorted form. 
# If the array contains less than two elements, return 0.
# You must write an algorithm that runs in linear time and uses linear extra space.

# leetcode - 164
# bucket sort

class Solution:
    # tc: O(n)
    # sc: O(n)
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0
        
        # 一些初始化
        max_ = max(nums)
        min_ = min(nums)
        max_gap = 0
        
        each_bucket_len = max(1,(max_-min_) // (len(nums)-1))
        buckets =[[] for _ in range((max_-min_) // each_bucket_len + 1)]
        
        # 把数字放入桶中
        for i in range(len(nums)):
            loc = (nums[i] - min_) // each_bucket_len
            buckets[loc].append(nums[i])

        print(buckets)
        
        # 遍历桶更新答案
        prev_max = float('inf')
        for i in range(len(buckets)):
            if buckets[i] and prev_max != float('inf'):
                max_gap = max(max_gap, min(buckets[i])-prev_max)
            
            if buckets[i]:
                prev_max = max(buckets[i])
                
        return max_gap
        
nums = [6,7,1,2,4,10,90]
s = Solution()

r = s.maximumGap(nums)

print(r)