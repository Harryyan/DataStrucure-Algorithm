# Q2:
# 统计一个数字在排序数组中出现的次数

import time


def count_numbers_in_sorted_array(items, target):
    low_index = find_lower(items, target)
    high_index = find_higher(items, target)

    return high_index - low_index


def find_lower(items, target):
    start = 0
    end = len(items) - 1

    while start <= end:
        m = (start + end) // 2
        if items[m] < target:
            start += 1
        else:
            end = m - 1

    return end


def find_higher(items, target):
    start = 0
    end = len(items) - 1

    while start <= end:
        m = (start + end) // 2

        if items[m] <= target:
            start += 1
        else:
            end = m - 1

    return end


target = 8
items = [1, 2, 3, 4, 4, 5, 5, 6, 6, 6, 7, 8, 8, 8, 10]
result = count_numbers_in_sorted_array(items, target)

print(result)
