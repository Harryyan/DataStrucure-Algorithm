# 给你两个整数 left 和 right ，表示区间 [left, right] ，
# 返回此区间内所有数字 按位与 的结果（包含 left 、right 端点）。

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        t = 0   
        while m < n:
            m = m >> 1
            n = n >> 1
            t += 1
        return m << t
    
n1 = 2
n2 = 4

s = Solution()

r = s.rangeBitwiseAnd(n1, n2)
print(r)