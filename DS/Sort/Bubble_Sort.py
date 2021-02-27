def sort_bubble(items):
    length = len(items) - 1
    for i in range(0, length):
        for j in range(0, length - i):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]

    return items


items = [4, 6, 1, 33, 88, 0, -4, 90]


print(sort_bubble(items))
