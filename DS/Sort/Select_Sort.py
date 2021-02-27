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
