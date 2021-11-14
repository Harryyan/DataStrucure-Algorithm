# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
# Given two integers x and y, return the Hamming distance between them.

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
