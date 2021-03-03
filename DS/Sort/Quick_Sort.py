def quick_sort(items, start, end):
    if end - start == 1:
        return

    if start < end:
        base = items[start]
        j = end - 1

        for i in range(start, end):
            if items[i] > base:
                while j > i:
                    if items[j] < base:
                        items[i], items[j] = items[j], items[i]
                        break
                    j -= 1

            if i == j:
                items.insert(i, base)
                items.pop(start)
                if items[i] < items[i - 1]:
                    items[i], items[i - 1] = items[i - 1], items[i]

        quick_sort(items, start, i)
        quick_sort(items, i, end - 1)


def quick_sort2_better(alist, first, last):
    if first > last:
        return

    mid_value = alist[first]
    low = first
    high = last

    while low < high:
        while low < high and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]

        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]

    alist[low] = mid_value
    quick_sort2_better(alist, first, low - 1)
    quick_sort2_better(alist, low + 1, last)


items = [9, 8, 7, 6, 5, 4]
items2 = [26, 45, 44, 6, 9, 54, 93]

quick_sort2_better(items2, 0, len(items2) - 1)

print(items2)

# 最好情况: O(nlogn)
# 最坏情况: O（n²）
# 平均情况: O(nlogn)
# 稳定性: 不稳定
# 辅助空间: O(logn) - O(n)
