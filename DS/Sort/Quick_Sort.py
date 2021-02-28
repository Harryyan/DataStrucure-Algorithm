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
                print(i)
                items.insert(i, base)
                items.pop(start)

                print("here")

                if items[i] < items[i - 1]:
                    items[i], items[i - 1] = items[i - 1], items[i]

        print(items)
        quick_sort(items, start, i)
        quick_sort(items, i, end - 1)


items = [9, 8, 7, 6, 5, 4]
#items2 = [26, 45, 44, 6, 9, 54, 93]

quick_sort(items, 0, len(items))
print(items)
