def insertion_sort(items):
    for i in range(1, len(items)):
        for j in range(0, i):
            if items[i] < items[j]:
                temp = items[i]
                items.pop(i)
                items.insert(j, temp)
    return items


items = [88, 83, 10, 9, 8, 7, 5, 5, 4, 3, 2, 1]

print(insertion_sort(items))
