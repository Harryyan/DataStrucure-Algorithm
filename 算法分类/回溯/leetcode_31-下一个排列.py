from typing import List

# Find the largest index k such that a[k] < a[k + 1]. If no such index exists, the permutation is the last permutation.
# Find the largest index l greater than k such that a[k] < a[l].
# Swap the value of a[k] with that of a[l].
# Reverse the sequence from a[k + 1] up to and including the final element a[n].

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        firstIndex = -1
        n = len(nums)
        def reverse(nums, i, j):
            while i < j:
                nums[i],nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        
        
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                firstIndex = i
                break
            
        if firstIndex == -1:
            reverse(nums, 0, n-1)
            return 
        secondIndex = -1
        
        for i in range(n-1, firstIndex, -1):
            if nums[i] > nums[firstIndex]:
                secondIndex = i
                break
            
        nums[firstIndex],nums[secondIndex] = nums[secondIndex], nums[firstIndex]
        reverse(nums, firstIndex+1, n-1)
        
        print(nums)

    
s = Solution()
nums = [1,8,7,6,5,4,3,2]

r = s.nextPermutation(nums)

print(r)