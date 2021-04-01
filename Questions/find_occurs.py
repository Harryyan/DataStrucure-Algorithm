# leetcode 39

def majorityElement(list):
    if not list:
        return None

    if len(list) == 1:
        return list[0]

    half_len = len(list) // 2
    hash_table = {}
    i = 0

    for item in list:
        if item not in hash_table:
            hash_table[item] = 1
        else:
            hash_table[item] += 1

            if hash_table[item] > half_len:
                return item


def majorityElement_Sort(nums):
    if not nums:
        return None

    # Timsort
    nums.sort()

    return nums[len(nums) // 2]


list = [1, 2, 3, 3, 3, 3, 3, 8]
result = majorityElement(list)

print(result)
