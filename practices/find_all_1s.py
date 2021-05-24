# 请实现一个函数，输入一个整数(以二进制串形式),
# 输出该数二进制表示中 1 的个数。例如，把 9 表示成二进制是 1001，有 2 位是 1。因此，如果输入 9，则该函数输出 2。
def hammingWeight(n):
    num = 0
    while n > 0:
        n = n & (n - 1)
        num += 1

    return num


result = hammingWeight(0b01100111)
print(result)