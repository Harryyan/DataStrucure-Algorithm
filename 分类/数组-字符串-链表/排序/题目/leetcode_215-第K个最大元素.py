from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()

        print(nums)
        n = len(nums)
        rest = n - k

        return nums[rest]
    
    
    
class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 使用堆
        return 0

s = Solution()
nums = [3,2,3,1,2,4,5,5,6]
k = 4

r = s.findKthLargest(nums, k)

print(r)