# Q1:
# 一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内
# 在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字


def find_missing_number(numbers):
    start = 0
    end = len(numbers) - 1

    while start <= end:
        m = (start + end) // 2
        if numbers[m] != m:
            return m
        else:
            start += 1

    return None


numbers = [0, 1, 2, 3, 4, 5, 6, 8]
result = find_missing_number(numbers)

print(result, end=" ")
