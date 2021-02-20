
# 对于队列来说，入队和出队总有一个时间复杂度是O(n)
# 这时候就要看你的操作，是出队操作多还是入队操作多
# 优化选择

class Queue:

    def __init__(self):
        self.__content = []

    def enqueue(self, value):
        self.__content.append(value)
        #self.__content.insert(0, value)

    def dequeue(self):
        if self.is_empty():
            return None

        self.__content.pop(0)
        # self.__content.pop()

    def size(self):
        return len(self.__content)

    def is_empty(self):
        return not self.__content

    def print(self):
        print(self.__content)


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)

    queue.print()

    queue.dequeue()

    queue.print()
