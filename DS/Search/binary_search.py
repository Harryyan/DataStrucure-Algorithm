def binary_Search(items, start, end, target):
    if start >= end:
        if items[end] == target:
            return True
        else:
            return False

    mid = start + (end - start) // 2

    if target <= items[mid]:
        return binary_Search(items, 0, mid, target)
    else:
        return binary_Search(items, mid + 1, end, target)


test = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = binary_Search(test, 0, len(test) - 1, 89)

print(result)
