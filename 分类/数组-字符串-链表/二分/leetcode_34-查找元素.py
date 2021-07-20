from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1, -1]
        
        result = [-1, -1]
        
        result[0] = self.find_1st_value(nums, 0, len(nums)-1, target)
        result[1] = self.find_last_value(nums, 0, len(nums)-1, target)
        
        return result

    def find_1st_value(self, items, start, end, target):
        if start == end:
            if items[start] == target:
                return start
            else:
                return -1

        mid = start + ((end - start) >> 1)

        # 关键: 只要是小于或者等于，就一直往前找
        if target <= items[mid]:
            # 关键 mid
            return self.find_1st_value(items, 0, mid, target)
        else:
            return self.find_1st_value(items, mid + 1, end, target)

    # 变体问题2: 查找最后一个等于给定值的元素


    def find_last_value(self, items, start, end, target):
        if end - start <= 1:
            if items[end] == target:
                return end
            elif items[start] == target:
                return start
            else:
                return -1

        mid = start + ((end - start) >> 1)

        # 关键
        if target < items[mid]:
            return self.find_last_value(items, 0, mid - 1, target)
        else:
            # 关键 mid
            return self.find_last_value(items, mid, end, target)
        
        
nums = [5,7,7,8,8,10]
target = 90
s = Solution()

r = s.searchRange(nums, target)

print(r)