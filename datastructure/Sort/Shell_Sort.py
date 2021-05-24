def shell_sort(items):
    length = len(items)
    gap = length // 2

    while gap > 0:
        for i in range(gap, length):
            j = i
            while j - gap >= 0:
                if items[j] < items[j - gap]:
                    items[j], items[j - gap] = items[j - gap], items[j]
                else:
                    break
                j -= gap
        gap //= 2

    return items


items = [88, 83, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print(shell_sort(items))

# 最好情况: 视gap值而定
# 最坏情况: O（n²）
# 平均情况: O(nlogn) ~ O(n²)
# 稳定性: 不稳定
# 辅助空间: O(1)
