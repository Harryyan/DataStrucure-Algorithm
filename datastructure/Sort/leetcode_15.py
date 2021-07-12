from typing import List

# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 
# a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

# 注意：答案中不可以包含重复的三元组。


# 解题思路1：排序 + 双指针


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        n=len(nums)
        res=[]
        if(not nums or n<3):
            return []
        nums.sort()
        res=[]
        for i in range(n):
            if(nums[i]>0):
                return res
            # 第一步去重，遇到相同的元素，直接跳过，避免重复
            if(i>0 and nums[i]==nums[i-1]):
                continue
            L=i+1
            R=n-1
            while(L<R):
                if(nums[i]+nums[L]+nums[R]==0):
                    res.append([nums[i],nums[L],nums[R]])
                    
                    # 同理，从左边起，若下一个元素和当前元素相同，跳到下一个；
                    while(L<R and nums[L]==nums[L+1]):
                        L=L+1
                        
                    # 同理，从右边起，若下一个元素和当前元素相同，跳到下一个；
                    while(L<R and nums[R]==nums[R-1]):
                        R=R-1
                    L=L+1
                    R=R-1
                elif(nums[i]+nums[L]+nums[R]>0):
                    R=R-1
                else:
                    L=L+1
        return res
    
    
nums = [-1,0,1,2,-1,-4]
s = Solution()

print(s.threeSum(nums))