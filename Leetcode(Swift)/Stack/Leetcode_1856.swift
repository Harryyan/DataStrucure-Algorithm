import Foundation

class Solution_1856 {
    // tc: O(n)
    // sc: O(n)
    // time: 15 mins BF but timeout
    // Solution: 2 stacks
    func maxSumMinProduct(_ nums: [Int]) -> Int {
        var nums = [0] + nums + [0]
        var preSum = [0]

        for i in nums {
            let pre = preSum.last!
            preSum.append(pre + i)
        }

        var right_first_smaller = Array(repeating: -1, count:nums.count)
        var left_first_smaller = Array(repeating: -1, count:nums.count)
        var stack: [Int] = []

        for i in 0..<nums.count {
            while stack.count>0 && nums[i]<nums[stack.last!] {
                right_first_smaller[stack.removeLast()] = i
            }
            stack.append(i)
        }

        stack = []

        for j in stride(from: nums.count-1, through: 0, by: -1) {
            while stack.count>0 && nums[j]<nums[stack.last!] {
                left_first_smaller[stack.removeLast()] = j
            }
            stack.append(j)
        }

        var res = 0
        for i in 1..<nums.count-1 {
            let left = left_first_smaller[i]
            let right = right_first_smaller[i]
            res = max(res, nums[i]*(preSum[right]-preSum[left+1]))
        }

        return res % (1000000007)
    }
}

// class Solution:
//     def maxSumMinProduct(self, nums: List[int]) -> int:
//         # 左右添加两个哨兵，方便单调栈内的判断
//         nums = [0] + nums + [0]
//         # 前缀和
//         presum = [0]
//         for n in nums:
//             presum.append(presum[-1] + n)
        
//         # 右边第一个比它小的元素下标
//         right_first_smaller = [None] * len(nums)
//         stack = []
//         for i in range(len(nums)):
//             # 如果当前元素比栈顶元素小，弹栈
//             while stack and nums[i] < nums[stack[-1]]:
//                 right_first_smaller[stack.pop()] = i
//             stack.append(i)

//         # 左边第一个比它小的元素下标
//         left_first_smaller = [None] * len(nums)
//         stack = []
//         for i in range(len(nums)-1,-1,-1):
//             # 如果当前元素比栈顶元素小，弹栈
//             while stack and nums[i] < nums[stack[-1]]:
//                 left_first_smaller[stack.pop()] = i
//             stack.append(i)

//         # 打擂台得到答案
//         res = 0
//         for i in range(1,len(nums)-1):
//             left = left_first_smaller[i]
//             right = right_first_smaller[i]
//             res = max(res, nums[i] * (presum[right] - presum[left+1]))
//         return res % (10 ** 9 + 7)
