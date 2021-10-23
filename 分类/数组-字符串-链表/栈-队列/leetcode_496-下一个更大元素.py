from typing import List

# leetcode - 496

# 给你两个 没有重复元素 的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。
# 请你找出 nums1 中每个元素在 nums2 中的下一个比其大的值。
# nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出 -1 。

class Solution:
    # 时间复杂度: O(mn)
    # 空间复杂度: O(n)
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = len(nums1)
        n = len(nums2)

        dict = {}
        ans = []
        
        for i in range(0, n):
            dict[nums2[i]] = i

        for i in range(0, m):
            startIndex = dict[nums1[i]] + 1

            if startIndex > n - 1:
                ans.append(-1)
                continue
            
            for j in range(startIndex, n):
                if nums2[j] > nums1[i]:
                    ans.append(nums2[j])
                    break
                else:
                    if j == n - 1:
                        ans.append(-1)

        return ans

class Solution_ACE:
    # 时间复杂度: O(mn) - 我觉得不是官方说的O(m+n), while循环中，得循环pop出旧的元素；
    # 空间复杂度: O(n)
    def nextGreaterElement(self, nums1, nums2):
        dic, stack = {}, []

        for i in range(len(nums2) - 1, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
                
            if stack: 
                dic[nums2[i]] = stack[-1]

            stack.append(nums2[i])

        return [dic.get(x, -1) for x in nums1]

num1 = [2,4]
nums2 = [3,4,2,1]

s = Solution_ACE()
s.nextGreaterElement(num1, nums2)