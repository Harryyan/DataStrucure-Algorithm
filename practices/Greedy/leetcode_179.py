#给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。

from typing import DefaultDict, List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if len(nums) == 1: return str(nums[0])

        self.quick_sort2_better(nums, 0, len(nums) - 1)
        nums.reverse()

        string_ints = [str(int) for int in nums]
        
        return "".join(string_ints)
        
    def quick_sort2_better(self, alist, first, last):
        if first > last:
            return

        mid_value = alist[first]
        low = first
        high = last
        
        
        # test = self.isGreater('3', '34')
        # print(test)
        
        while low < high:
            while low < high and self.isGreater(str(alist[high]), str(mid_value)):
                high -= 1
            alist[low] = alist[high]
            
            
            print(low, end="\t")
            print(high)
            
            while low < high and self.isGreater(str(alist[low]), str(mid_value)) == False:
                low += 1
            alist[high] = alist[low]

        alist[low] = mid_value
        self.quick_sort2_better(alist, first, low - 1)
        self.quick_sort2_better(alist, low + 1, last)
    
    def isGreater(self, str1, str2):
        n = len(str1)
        m = len(str2)
        
        if n == m:
            return int(str1) >= int(str2)
        
        num = max(n, m)
        
        for i in range(0, num):
            x = str1[i if i < len(str1) - 1 else len(str1) - 1]
            y = str2[i if i < len(str2) - 1 else len(str2) - 1]
            
            if x == y: continue
            
            if int(x) > int(y): return True
            
            if int(x) < int(y): return False
            
s = Solution()
sample = [1332, 7]
result = s.largestNumber(sample)

print(result)