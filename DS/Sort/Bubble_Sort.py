def sort_bubble(items):
    length = len(items) - 1
    for i in range(0, length):
        for j in range(0, length - i):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
    return items


items = [88, 83, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print(sort_bubble(items))
