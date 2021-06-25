# 给定一个非负整数数组，你最初位于数组的第一个位置。
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 你的目标是使用最少的跳跃次数到达数组的最后一个位置。
# 假设你总是可以到达数组的最后一个位置。

class Solution:
    min_jump = float('inf')
    count = 0
    
    def canJump(self, nums) :
        for i, jump in enumerate(nums):   
            s = self.forwards(i, jump, nums) + i
            self.min_jump = min(self.min_jump, s)
            
            if i >= self.min_jump:
                break
            
            self.count = 0
            
        return self.min_jump
    
    def forwards(self, start, jump, nums) -> int:
        n = len(nums) - 1
        newStart = start+jump
        
        if start > n or newStart == start: self.count = float('inf'); return self.count
        
        if newStart == n:
            self.count += 1
        
        if newStart < n:
            self.count += 1
            self.forwards(newStart, nums[newStart], nums)
        
        return self.count
    
s = Solution()
nums = [2,3,1,1,4]
result = s.canJump(nums)
print(result)
