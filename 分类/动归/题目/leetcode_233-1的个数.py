# 给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。
# LeetCode- 233

class Solution_OverTime:
    # 该解法超出时间限制; 但算是经典dp思路： 画出状态matrix，遍历
    # 时间复杂度: O(mn/10) 约等于 0(n) - 该题目标应该是最对O(logn)时间复杂度
    # 空间复杂度: O(1)
    def countDigitOne(self, n: int) -> int:
        # edge condition
        if n == 0: return 0
        if n < 10: return 1

        row = n // 10

        # initial values
        dp = [1] * 10
        dp[0] = 0

        for i in range(1, row+1):
            prefix = str(i)
            new_count = dp[9]

            for j in range(0,10):
                # 重复计算颇多
                value = prefix + str(j)
                count_1 = value.count("1")

                if j == 0:
                    dp[j] = new_count + count_1
                else:
                    dp[j] = count_1 + dp[j - 1]

        return dp[n % 10]

# 将 1 ~ n 的个位、十位、百位、...的 1 出现次数相加，即为 1 出现的总次数。

class Solution:
    # 时间复杂度 O(logn) 
    # 空间复杂度 O(1)
    def countDigitOne(self, n: int) -> int:
        digit, res = 1, 0
        high, cur, low = n // 10, n % 10, 0

        while high != 0 or cur != 0: # 当 high 和 cur 同时为 0 时，说明已经越过最高位，因此跳出
            low += cur * digit # 将 cur 加入 low ，组成下轮 low
            cur = high % 10 # 下轮 cur 是本轮 high 的最低位
            high //= 10 # 将本轮 high 最低位删除，得到下轮 high
            digit *= 10 # 位因子每轮 × 10

            low += cur * digit
            cur = high % 10
            high //= 10
            digit *= 10

        return res

n = 1453
s = Solution()

r = s.countDigitOne(n)
print(r)