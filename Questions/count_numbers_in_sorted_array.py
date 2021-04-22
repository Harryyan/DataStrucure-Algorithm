# Q1:
# 统计一个数字在排序数组中出现的次数

def count_numbers_in_sorted_array(items, target):
    left = 0
    right = len(items) - 1

    while left <= right:
        mid = (left + right) // 2

        if items[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1

    return left


target = 4
items = [1, 3, 3, 3, 4]
result = count_numbers_in_sorted_array(items, target)
result1 = count_numbers_in_sorted_array(items, target - 1)

print(result - result1)
