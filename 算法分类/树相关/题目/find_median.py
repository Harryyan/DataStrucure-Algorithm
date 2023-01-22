import heapq

# 如果是前40%的数据，则要保证大顶堆凑够前40%的数据，直接pop出来
class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        # 初始化大顶堆和小顶堆
        self.max_heap = []
        self.min_heap = []

    # Python 默认提供小顶堆实现
    def addNum(self, num: int) -> None:
        # 先加到小顶堆，再把小堆顶元素加到大顶堆
        if len(self.max_heap) == len(self.min_heap):
            heapq.heappush(self.max_heap, -heapq.heappushpop(self.min_heap, num))
        else:
            # 先加到大顶堆，再把大堆顶元素加到小顶堆
            heapq.heappush(self.min_heap, -heapq.heappushpop(self.max_heap, -num))

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return -self.max_heap[0]


test = MedianFinder()
test.addNum(1)

print(test.findMedian())
