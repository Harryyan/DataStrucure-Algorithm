# Q1:
# 一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内
# 在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字


def find_missing_number(numbers):
    start = 0
    end = len(numbers)

    while start < end:
        m = (start + end) // 2
        if numbers[m] == m:
            start += 1
        else:
            end = m

    return start


numbers = [0, 2, 3]
result = find_missing_number(numbers)

print(result, end=" ")
