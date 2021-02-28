# 不稳定排序 （考虑每次寻找最大值）

def selection_sort(items):
    for i in range(0, len(items)):
        temp = i
        min = items[temp]
        for j in range(i, len(items)):
            if min > items[j]:
                min = items[j]
                temp = j
        items[i], items[temp] = items[temp], items[i]
    return items


items = [88, 83, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print(selection_sort(items))

# 最好情况: O(n²)
# 最坏情况: O（n²）
# 平均情况: O(n²)
# 稳定性: 不稳定
# 辅助空间: O(1)
