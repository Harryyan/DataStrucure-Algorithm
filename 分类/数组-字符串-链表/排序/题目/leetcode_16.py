from typing import List
import collections

# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。
# 找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        result = float('inf')
        min_test = float('inf')
        
        n=len(nums)
        nums.sort()

        for i in range(n):
            L=i+1
            R=n-1
            
            while(L<R):
                print(nums[i]+nums[L]+nums[R])
                if abs(nums[i]+nums[L]+nums[R]-target) < min_test:
                        result = nums[i]+nums[L]+nums[R]
                        min_test = abs(nums[i]+nums[L]+nums[R]-target)
                        
                if(nums[i]+nums[L]+nums[R]==target):
                    result = target
                    return result
                elif(nums[i]+nums[L]+nums[R] > target):
                    R=R-1
                else:
                    L=L+1
                    
        return result
    
nums = [1,2,4,8,16,32,64,128]
target = 82

s= Solution()
r = s.threeSumClosest(nums, target)

print(r)