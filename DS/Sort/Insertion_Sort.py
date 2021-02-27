def insertion_sort(items):
    for i in range(1, len(items)):
        temp = i
        for j in range(i - 1, -1, -1):
            if items[temp] < items[j]:
                items[temp], items[j] = items[j], items[temp]
                temp = j
            print(items)
    return items


items = [88, 83, 10, 9, 8, 7, 5, 5, 4, 3, 2, 1]

print(insertion_sort(items))
