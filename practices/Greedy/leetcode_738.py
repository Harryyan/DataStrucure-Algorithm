from typing import List

# 给定一个非负整数 N，找出小于或等于 N 的最大的整数，同时这个整数需要满足其各个位数上的数字是单调递增。

#（当且仅当每个相邻位数上的数字 x 和 y 满足 x <= y 时，我们称这个整数是单调递增的。）

# 示例 1:

# 输入: N = 10
# 输出: 9
# 示例 2:

# 输入: N = 1234
# 输出: 1234
# 示例 3:

# 输入: N = 332
# 输出: 299

class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        if n < 10: return n
        if 11 < n < 20 or n == 10: return 9
        if n == 11: return 11
        
        nums_str = str(n)
        nums = list(map(int, nums_str))
        index = 0
        
        for i in range(1, len(nums)):
            if nums_str[i] > nums_str[i-1]:
                index = i
            elif nums_str[i] == nums_str[i-1]:
                continue
            else:
                nums[index] -= 1
                nums[index+1:] = [9] * (len(nums) - index - 1)
                
                break
        i = 0
        while nums[i] == 0:
            i += 1
        
        nums_str = list(map(str, nums[i:]))
        return int("".join(nums_str))
    
s = Solution()
r = s.monotoneIncreasingDigits(12345)
print(r)