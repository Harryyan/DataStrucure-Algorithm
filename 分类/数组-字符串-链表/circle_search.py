# 如果有序数组是一个循环有序数组，比如 4，5，6，1，2，3。
# 针对这种情况，如何实现一个求“值等于给定值”的二分查找算法呢？


# Solution_1:
# 1. 找到分界下标，分成两个有序数组
# 2. 判断目标值在哪个有序数据范围内，做二分查找


# Solution_2:
# 循环数组存在一个性质：以数组中间点为分区，会将数组分成一个有序数组和一个循环有序数组。

# 如果首元素小于 mid，说明前半部分是有序的，后半部分是循环有序数组；
# 如果首元素大于 mid，说明后半部分是有序的，前半部分是循环有序的数组；
# 如果目标元素在有序数组范围中，使用二分查找；
# 如果目标元素在循环有序数组中，设定数组边界后，使用以上方法继续查找。

def circle_search(items, start, end, target):
    if start > end:
        return -1

    mid = start + ((end - start) >> 1)

    if items[start] <= items[mid]:
        if items[start] <= target <= items[mid]:
            return binary_Search(items, start, mid, target)
        else:
            return circle_search(items, mid + 1, end, target)
    elif items[start] > items[mid]:
        if items[mid] <= target <= items[end]:
            return binary_Search(items, mid, end, target)
        else:
            return circle_search(items, start, mid - 1, target)


def binary_Search(items, start, end, target):
    if start >= end:
        if items[end] == target:
            return end
        else:
            return -1

    mid = start + ((end - start) >> 1)

    if target <= items[mid]:
        return binary_Search(items, start, mid, target)
    else:
        return binary_Search(items, mid + 1, end, target)


sample = [14, 15, 1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 88
result = circle_search(sample, 0, len(sample) - 1, target)

print(result)
