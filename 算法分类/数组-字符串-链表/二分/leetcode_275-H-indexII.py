from typing import List

# Given an array of integers citations where citations[i] is the number of citations a researcher received for their 
# ith paper and citations is sorted in an ascending order, return compute the researcher's h-index.
# According to the definition of h-index on Wikipedia: A scientist has an index h if 
# h of their n papers have at least h citations each, and the other n − h papers have no more than h citations each.
# If there are several possible values for h, the maximum one is taken as the h-index.
# You must write an algorithm that runs in logarithmic time.


class Solution:
    # tc: O(logn)
    # sc: O(1)
    def hIndex(self, citations: List[int]) -> int:
        low = 0
        n = len(citations)
        high = n - 1

        while low <= high:
            mid = low + ((high - low) >> 1)

            if citations[mid] == n - mid:
                return citations[mid]

            if citations[mid] > n - mid:
                high = mid - 1

            if mid < n - citations[mid]:
                low = mid + 1

        return n - low

citations = [0,1,3,5,6]
s = Solution()

r = s.hIndex(citations)

print(r)