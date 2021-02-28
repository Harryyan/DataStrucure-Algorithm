# 稳定的排序

def insertion_sort(items):
    for i in range(1, len(items)):
        temp = i
        for j in range(i - 1, -1, -1):
            if items[temp] < items[j]:
                items[temp], items[j] = items[j], items[temp]
                temp = j
            else:
                continue
    return items


def insertion_sort_1(items):
    for i in range(1, len(items)):
        for j in range(0, i):
            if items[i] < items[j]:
                temp = items[i]
                items.pop(i)
                items.insert(j, temp)
            else:
                continue
    return items


items = [88, 83, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print(insertion_sort(items))

# 最好情况: 根据gap不同而不同
# 最坏情况: O（n²）
# 平均情况: O(nlogn - n²)
# 稳定性: 不稳定
# 辅助空间: O(1)
