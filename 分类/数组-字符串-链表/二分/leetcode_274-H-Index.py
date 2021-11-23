from typing import List

# Given an array of integers citations where citations[i] is the number of citations a researcher received for their 
# ith paper, return compute the researcher's h-index.
# According to the definition of h-index on Wikipedia: A scientist has an
# index h if h of their n papers have at least h citations each, and the other n − h papers have no more than h citations each.
# If there are several possible values for h, the maximum one is taken as the h-index.


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        low = 0
        n = len(citations)
        high = n - 1

        citations.sort()

        while low <= high:
            mid = low + ((high - low) >> 1)

            if citations[mid] == n - mid:
                return citations[mid]

            if citations[mid] > n - mid:
                high = mid - 1

            if mid < n - citations[mid]:
                low = mid + 1

        return n - low

citations = [1,3,1]
s = Solution()

r = s.hIndex(citations)

print(r)