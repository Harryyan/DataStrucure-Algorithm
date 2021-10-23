from typing import List

# leetcode - 496

# 给你两个 没有重复元素 的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。
# 请你找出 nums1 中每个元素在 nums2 中的下一个比其大的值。
# nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出 -1 。

class Solution:
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

num1 = [2,4]
nums2 = [1,2,3,4]

s = Solution()
s.nextGreaterElement(num1, nums2)