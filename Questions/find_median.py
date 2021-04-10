class MedianFinder:
    def __init__(self):
        self.items = []

    def addNum(self, num: int) -> None:
        self.items.append(num)

    def findMedian(self) -> float:
        if self.items is None:
            return 0.0

        if len(self.items) == 1:
            return self.items[0]

        if len(self.items) == 2:
            return (self.items[0] + self.items[1]) / 2

        self.items.sort()

        if len(self.items) % 2 == 0:
            first = len(self.items) // 2 - 1
            end = first + 1

            return (self.items[first] + self.items[end]) / 2
        else:
            index = len(self.items) // 2
            return self.items[index]


median = MedianFinder()
median.addNum(1)
median.addNum(3)
median.addNum(7)
print(median.findMedian())
median.addNum(4)
median.addNum(3)
median.addNum(2)
median.addNum(1)
median.addNum(33)

print(median.findMedian())
