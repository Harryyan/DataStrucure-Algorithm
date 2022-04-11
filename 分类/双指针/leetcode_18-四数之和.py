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

# 排序 +双指针
class Soluction_Advanced:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
         ans = []
         if len(nums) < 4:
            return ans;
        
         nums.sort()
         length = len(nums)
         
         for i in range(length):
             if nums[i] > 0 and target < 0:
                    break
                
             if i > 0 and nums[i] == nums[i-1]:
                continue
                
             for j in range(i+1, length):
                 if j > i+1 and nums[j] == nums[j-1]:
                        continue
                 two_sum = nums[i] + nums[j]
                
                 if two_sum > 0 and target < 0:
                    break

                 left, right = j + 1, length - 1
        
                 while left < right:
                    four_sum = two_sum + nums[left] + nums[right]
                    # residual = target - nums[i] - nums[j] - nums[left] - nums[right]
                    if four_sum == target:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif four_sum < target:
                        left += 1
                    else:
                        right -= 1
        
             return ans

# 多数之和 - 使用递归
class Solution_NSum:
        def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
            def nSum(nums: List[int], n: int, target: int) -> List[List[int]]:
                res = []
                if len(nums) < n:
                    return res
                if n == 2:
                    left, right = 0, len(nums) - 1
                    while left < right:
                        if nums[left] + nums[right] == target:
                            res.append([nums[left], nums[right]])
                            while left < right and nums[left] == nums[left+1]:
                                left += 1
                            while left < right and nums[right] == nums[right-1]:
                                right -= 1
                            left += 1
                            right -= 1
                        elif nums[left] + nums[right] < target:
                            left += 1
                        else:
                            right -= 1
                    return res
                else:
                    for i in range(len(nums)-n+1):
                        if i > 0 and nums[i] == nums[i-1]:
                            continue
                        min_sum = sum(nums[i:i+n])
                        if min_sum > target:
                            break
                        max_sum = nums[i] + sum(nums[-n+1:])
                        if max_sum < target:
                            continue
                        sub_res = nSum(nums[i+1:], n-1, target-nums[i])
                        for j in range(len(sub_res)):
                            res.append([nums[i]]+sub_res[j])
                    return res
                    
            nums.sort()
            res = nSum(nums, 4, target)
            return res 
    
    
nums = [1,-2,-5,-4,-3,3,3,5]
target = -11
s = Solution_NSum()

print(s.fourSum(nums, target))