# 稳定的排序算法
def sort_bubble(items):
    length = len(items) - 1
    for i in range(0, length):
        for j in range(0, length - i):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
    return items


items = [88, 83, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print(sort_bubble(items))


# 最好情况: O(n)
# 最坏情况: O（n²）
# 平均情况: O(n²)
# 稳定性: 稳定
# 辅助空间: O(1)
