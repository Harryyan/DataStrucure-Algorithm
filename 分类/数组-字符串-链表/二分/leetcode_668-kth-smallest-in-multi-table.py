# Nearly everyone has used the Multiplication Table. The multiplication table of size m x n 
# is an integer matrix mat where mat[i][j] == i * j (1-indexed).
# Given three integers m, n, and k, return the kth smallest element in the m x n multiplication table.

# leetcode - 668

class Solution:
    # tc: O(logmn * m)
    # sc: O(1)
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        left, right = 1, m * n 

        while left < right:
            mid = left + (right-left) // 2
            cnt = 0

            # optimize - reduce some iteration
            start = mid // n
            cnt += start * n

            for i in range(start+1, m+1):
                cnt += mid // i

            if cnt < k:
                left = mid + 1
            else:
                right = mid

        return left

s = Solution()
r = s.findKthNumber(4,4,5)

print(r)