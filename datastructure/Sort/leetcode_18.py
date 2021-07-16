from typing import List
import collections


# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，
# 使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

# 注意：答案中不可以包含重复的四元组。


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        res=[]
        if(not nums or n<4):
            return []
        nums.sort()
        res=[]
        
        for i in range(n):
            if(i>0 and nums[i]==nums[i-1]):
                continue
            
            for j in range(i+1, n):
                L=j+1
                R=n-1
                
                if(j>0 and nums[j]==nums[j-1] and j-1!=i):
                    continue
                
                while(L<R):
                    if(nums[i]+nums[j]+nums[L]+nums[R] == target):                        
                        res.append([nums[i], nums[j], nums[L], nums[R]])
                        
                        # 同理，从左边起，若下一个元素和当前元素相同，跳到下一个；
                        while(L<R and nums[L]==nums[L+1]):
                            L=L+1
                            
                        # 同理，从右边起，若下一个元素和当前元素相同，跳到下一个；
                        while(L<R and nums[R]==nums[R-1]):
                            R=R-1
                        L=L+1
                        R=R-1
                    elif(nums[i]+nums[j]+nums[L]+nums[R] > target):
                        R=R-1
                    else:
                        L=L+1
        return res
    
nums = [1,-2,-5,-4,-3,3,3,5]
target = -11
s = Solution()

print(s.fourSum(nums, target))