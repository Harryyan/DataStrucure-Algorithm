from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp=nums.copy()
        temp.sort()
        i=0
        j=len(nums)-1
        while i<j:
            if (temp[i]+temp[j])>target:
                j=j-1
            elif (temp[i]+temp[j])<target:
                i=i+1
            else:
                break

        p=nums.index(temp[i])
        nums.pop(p)
        k=nums.index(temp[j])
        if k>=p:
            k=k+1
        return [p,k]
    
    
nums = [3,2,4]
target = 6

s = Solution()
print(s.twoSum(nums, target))