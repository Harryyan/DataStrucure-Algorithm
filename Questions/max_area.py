# Q3:
# 给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点(i,ai).
# 在坐标内画 n 条垂直线，垂直线 i的两个端点分别为(i,ai) 和 (i, 0) .
# 找出其中的两条线，使得它们与x轴共同构成的容器可以容纳最多的水。说明：你不能倾斜容器


def max_area(items):
    start = 0
    end = len(items) - 1
    area = 0

    while start < end:
        height = 0
        interval = end - start

        if items[start] > items[end]:
            height = items[end]
            end -= 1
        else:
            height = items[start]
            start += 1

        temp = interval * height

        if temp > area:
            area = temp

    return area


items = [1, 8, 6, 2, 5, 4, 8, 3, 7]
result = max_area(items)

print(result)
