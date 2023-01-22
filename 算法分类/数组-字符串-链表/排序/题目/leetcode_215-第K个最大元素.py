from typing import List
import heapq as hq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()

        print(nums)
        n = len(nums)
        rest = n - k

        return nums[rest]
    
# 排序 ：时间复杂度 O(NlogN)，空间复杂度 O(1)  

# 也可以用快排
def quick_sort_search_kth(alist, first, last, k):
    if k > len(alist):
        return

    if first > last:
        return

    mid_value = alist[first]
    low = first
    high = last

    while low < high:
        while low < high and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]

        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]

    alist[low] = mid_value

    if low + 1 == k:
        print(alist[low])
        return
    elif low + 1 < k:
        quick_sort_search_kth(alist, low + 1, last, k)
    else:
        quick_sort_search_kth(alist, first, low - 1, k)

# 排序 ：时间复杂度 O(NlogN)，空间复杂度 O(1)  

class Solution_Heap:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 使用堆
        heap = []
        
        for num in nums:
            hq.heappush(heap, num)
            
            if len(heap) > k:
                hq.heappop(heap)
        
        return heap[0]
    
# 堆 ：时间复杂度 O(NlogK)，空间复杂度 O(K)。


s = Solution()
s1 = Solution_Heap()
nums = [3,2,3,1,2,4,5,5,6]
k = 4

r = s.findKthLargest(nums, k)

print(r)