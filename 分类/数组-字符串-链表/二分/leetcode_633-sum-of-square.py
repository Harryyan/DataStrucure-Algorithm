# Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.
# leetcode - 633

class Solution:
    # tc: O(n ** 0.5)
    # sc: O(1)
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(c ** 0.5) + 1
        
        # 双指针
        while left <= right:
            total = left ** 2 + right ** 2

            if total == c:
                return True
            elif total > c:
                right -= 1
            else:
                left += 1

        return False

c = 1000
s = Solution()

r = s.judgeSquareSum(c)
print(r)
