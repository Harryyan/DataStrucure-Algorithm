from typing import List

# 给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。

# 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

# 说明:

# 为什么返回数值是整数，但输出的答案是数组呢?

# 请注意，输入数组是以「引用」方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

# 你可以想象内部操作如下:

# // nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
# int len = removeDuplicates(nums);

# // 在函数里修改输入数组对于调用者是可见的。
# // 根据你的函数返回的长度, 它会打印出数组中 该长度范围内 的所有元素。
# for (int i = 0; i < len; i++) {
#     print(nums[i]);
# }


# 示例 1：

# 输入：nums = [1,1,2]
# 输出：2, nums = [1,2]
# 解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素。
# 示例 2：

# 输入：nums = [0,0,1,1,1,2,2,3,3,4]
# 输出：5, nums = [0,1,2,3,4]
# 解释：函数应该返回新的长度 5 ， 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4 。不需要考虑数组中超出新长度后面的元素。


class Solution1:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return 1
        
        pre = nums[0]
        
        i = 1
        while i < len(nums):
            if pre == nums[i]:
                nums.pop(i)
                continue  
                     
            pre = nums[i]
            i += 1 
            
        return len(nums)


# 双指针 -- 快，慢指针
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1
        
class Solution3:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        temp = 1

        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                if temp >= 2: temp = 1   

                i += 1
                nums[i] = nums[j]

                continue

            if nums[i] == nums[j] and temp < 2:
                temp += 1
                i += 1
                nums[i] = nums[j]

        print(nums)

        return i + 1

      
nums = [1,1,1,2,2,3]
s = Solution()

r = s.removeDuplicates(nums)

print(r)