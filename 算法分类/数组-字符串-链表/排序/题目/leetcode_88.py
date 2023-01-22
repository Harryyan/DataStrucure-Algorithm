from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        x = len(nums1)
        nums1[x-n:] = nums2[0:]
        
        nums1.sort()
        
        print(nums1)
        
        
s = Solution()
nums1 = [1]
m = 1
nums2 = []
n = 0

s.merge(nums1, m, nums2, n)