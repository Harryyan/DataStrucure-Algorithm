# 两个整数之间的 汉明距离 指的是这两个数字对应二进制位不同的位置的数目。
# 给你两个整数 x 和 y，计算并返回它们之间的汉明距离。

# leetcode - 461

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y
        count = 0

        while z != 0:
            if ((z & 1) == 1): count += 1
            z = z >> 1

        return count

s = Solution()
r = s.hammingDistance(1,4)
print(r)
