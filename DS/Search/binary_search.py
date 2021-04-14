# Limitations:
#
# 二分查找依赖数组，也就是顺序表结构
# 二分查找只针对有序数据，最好是静态数据，不会频繁插入和删除
# 数据量太大，太小都不适合二分查找；但是如果是复杂比较，例如比较长度为300
# 的字符串，使用二分查找能降低比较次数，提升性能
import time


def binary_Search(items, start, end, target):
    if start >= end:
        if items[end] == target:
            return True
        else:
            return False

    # 位运算速度快
    mid = start + ((end - start) >> 1)

    if target <= items[mid]:
        return binary_Search(items, 0, mid, target)
    else:
        return binary_Search(items, mid + 1, end, target)


# 变体问题1: 查找第一个等于给定值的元素


def find_1st_value(items, start, end, target):
    if start == end:
        if items[start] == target:
            return start
        else:
            return None

    mid = start + ((end - start) >> 1)

    # 关键: 只要是小于或者等于，就一直往前找
    if target <= items[mid]:
        # 关键 mid
        return find_1st_value(items, 0, mid, target)
    else:
        return find_1st_value(items, mid + 1, end, target)

# 变体问题2: 查找最后一个等于给定值的元素


def find_last_value(items, start, end, target):
    if end - start <= 1:
        if items[end] == target:
            return end
        elif items[start] == target:
            return start
        else:
            return None

    mid = start + ((end - start) >> 1)

    # 关键
    if target < items[mid]:
        return find_last_value(items, 0, mid - 1, target)
    else:
        # 关键 mid
        return find_last_value(items, mid, end, target)


# 变体问题3: 查找第一个大于或等于给定值的元素
def find_1st_equal_or_greater(items, target):
    low = 0
    high = len(items) - 1

    while low < high:
        mid = low + ((high - low) >> 1)

        if items[mid] < target:
            low = mid + 1
        elif items[mid] > target:
            high = mid
        else:
            if mid > 1 and items[mid - 1] < target:
                low = mid
                break
            else:
                high = max(0, mid - 1)

    if items[low] >= target:
        return low
    else:
        return -1


# 变体问题4: 查找最后一个小于或等于给定值的元素
def find_last_equal_or_less(items, target):
    low = 0
    high = len(items) - 1

    while low < high:
        mid = low + ((high - low) >> 1)

        if items[mid] < target:
            low = mid
        elif items[mid] > target:
            high = mid - 1
        else:
            if mid + 1 <= high and items[mid + 1] == target:
                low = mid + 1
            else:
                high = mid

        if low == high - 1:
            if items[high] <= target:
                low = high
            else:
                break

    if items[low] <= target:
        return low
    else:
        return -1


# main
sample = [1, 3, 4, 5, 7, 8, 8, 8, 11, 18]
target = 16
index = find_last_equal_or_less(sample, target)
print(index)
