def merge_sort(list):
    n = len(list)

    if n == 1:
        return list

    mid = n // 2

    left = merge_sort(list[:mid])
    right = merge_sort(list[mid:])

    left_cursor = 0
    right_cursor = 0
    result = []

    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] <= right[right_cursor]:
            result.append(left[left_cursor])
            left_cursor += 1
        else:
            result.append(right[right_cursor])
            right_cursor += 1
    result += left[left_cursor:]
    result += right[right_cursor:]

    return result


items = [26, 45, 44, 6, 9, 54, 93]

result = merge_sort(items)

print(result)

# 最好情况: O(nlogn)
# 最坏情况: O（nlogn）
# 平均情况: O(nlogn)
# 稳定性: 稳定
# 辅助空间: O(n)
