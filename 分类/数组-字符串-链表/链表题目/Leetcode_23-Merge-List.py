import ListNode
import heapq
from typing import List

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def __lt__(self,other):
            return self.val < other.val
        ListNode.__lt__ = __lt__
        heap = []
        for i in lists:
            if i :heapq.heappush(heap,i)
        d = c = ListNode(-1)
        while heap:
            n = heapq.heappop(heap)
            c.next = n
            c = c.next
            n = n.next
            if n:heapq.heappush(heap,n)
        return d.next
