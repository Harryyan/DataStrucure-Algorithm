from typing import List

# 给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        c = [0]*(m+n)
        
        i = 0
        j = 0
        k = 0
        
        while i < m and j < n:
            if nums1[i] >= nums2[j]:
                c[k] = nums2[j]
                j += 1
            else:
                c[k] = nums1[i]
                i += 1
            
            k += 1
        
        if i != m:
            c[k:] = nums1[i:]
        
        if j != n:
            c[k:] = nums2[j:]
            
        median = 0
        
        if len(c) == 0:
            return 0
        
        if len(c) % 2 == 0:
            index = len(c) // 2
            median = (c[index] + c[index-1]) / 2
        else:
            index = len(c) // 2
            median = c[index]
        
        return median


s = Solution()
nums1 = [2]
nums2 = []

result = s.findMedianSortedArrays(nums1, nums2)

print(result)