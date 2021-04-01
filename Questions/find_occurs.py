# leetcode 39

def majorityElement(nums):
    if not nums:
        return None

    nums.sort()

    return nums[len(nums) // 2]


list = [1, 2, 3, 4, 5, 6]
result = majorityElement(list)

print(result)
