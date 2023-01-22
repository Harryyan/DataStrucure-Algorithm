from typing import List

# 整数数组 nums 按升序排列，数组中的值 互不相同 。
# 在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，
# 使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。
# 给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。


class Solution:
    
    def circle_search(self, items, start, end, target):
        if start > end:
            return -1

        mid = start + ((end - start) >> 1)

        if items[start] <= items[mid]:
            if items[start] <= target <= items[mid]:
                return self.binary_Search(items, start, mid, target)
            else:
                return self.circle_search(items, mid + 1, end, target)
        elif items[start] > items[mid]:
            if items[mid] <= target <= items[end]:
                return self.binary_Search(items, mid, end, target)
            else:
                return self.circle_search(items, start, mid - 1, target)


    def binary_Search(self, items, start, end, target):
        if start >= end:
            if items[end] == target:
                return end
            else:
                return -1

        mid = start + ((end - start) >> 1)

        if target <= items[mid]:
            return self.binary_Search(items, start, mid, target)
        else:
            return self.binary_Search(items, mid + 1, end, target)
    
    def search(self, nums: List[int], target: int) -> int:
        return self.circle_search(nums, 0, len(nums)-1,target)
    
    
sample = [4,5,6,7,0,1,2]
target = 0

s = Solution()
r = s.search(sample, target)

print(r)