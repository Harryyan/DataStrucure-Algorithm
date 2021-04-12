# Limitations:
#
# 二分查找依赖数组，也就是顺序表结构
# 二分查找只针对有序数据，最好是静态数据，不会频繁插入和删除
# 数据量太大，太小都不适合二分查找；但是如果是复杂比较，例如比较长度为300
# 的字符串，使用二分查找能降低比较次数，提升性能

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


test = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = binary_Search(test, 0, len(test) - 1, 2)

print(result)
