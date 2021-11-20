# Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.
# leetcode - 633

class Solution:

    def sqrt(self, x):
        if x <= 1:
            return x

        left = 1
        right = x >> 1
        while left < right:
            mid = (left + right + 1) >> 1
            if mid * mid > x:
                right = mid - 1
            else:
                left = mid

        return left

    def judgeSquareSum(self, c: int) -> bool:
        if c == 0 or c == 1: return True

        temp = self.sqrt(c)
        if temp ** 2 == c: return True

        for i in range(temp, 0, -1):
            print(i)
            temp2 = c - i ** 2
            temp3 = self.sqrt(temp2)

            if temp3 ** 2 == temp2: return True

        return False

c = 1000
s = Solution()

r = s.judgeSquareSum(c)
print(r)
