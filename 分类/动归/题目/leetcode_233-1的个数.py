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


class Solution:
    def countDigitOne(self, n: int) -> int:
        if n==0: return 0
        if n<10: return 1

        m=len(str(n))  

        # dp[i] 小于等于i位数字的包含1的个数 (注意是1的个数 不是数字个数)
        dp=[0]*(m+1)
        for j in range(1,m+1):
            # 10**(j-1)对应第j位是1 剩余位置不包含1 dp[j-1]对应剩余的j-1位包含1 
            dp[j]=10**(j-1)+10*dp[j-1]
        # 计算
        total=0
        n_list=[int(c) for c in str(n)]
        # 小于n的数字: 最高位比n小 最高位相等第二位小 前两位相等第三位小...
        for j in range(m):
            for lower in range(n_list[j]):
                cnt_1_pre=sum([d==1 for d in n_list[0:j]])+int(lower==1)
                if cnt_1_pre!=0:
                    total+=cnt_1_pre*10**(m-(j+1))+dp[m-(j+1)] # 如果前序有1后面什么数字都可
                else:
                    total+=dp[m-(j+1)]
        
        # 加上等于n的情况
        total+=sum([d==1 for d in n_list])
        return total

n = 1000
s = Solution()

r = s.countDigitOne(n)
print(r)