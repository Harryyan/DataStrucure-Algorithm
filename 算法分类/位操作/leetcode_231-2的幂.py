# 给你一个整数 n，请你判断该整数是否是 2 的幂次方。如果是，返回 true ；否则，返回 false 。
# 如果存在一个整数 x 使得 n == 2x ，则认为 n 是 2 的幂次方。

# leetcode - 231

# lowbit 运算
# lowbit(n) = n & -n
# 证明：计算机知识，反码，补码
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & -n) == n


s = Solution()

r = s.isPowerOfTwo(32)
print(r)