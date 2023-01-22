class Solution:
    def climbStairs(self, n: int) -> int:
        hash_table = {}

        def f(n):
            if n == 1:
                return 1

            if n == 2:
                return 2

            value = 0
            if n in hash_table:
                return hash_table[n]
            else:
                value = f(n-1) + f(n-2)
                hash_table[n] = value

            return value

        return f(n)


solution = Solution()
print(solution.climbStairs(45))


# 还可以演化成 跳 1 ... n阶台阶
# 结果是 2的n-1次方
