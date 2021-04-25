# 仅使用两个栈实现先入先出队列。队列应当支持一般队列支持的所有操作（push、pop、peek、empty）


class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_1 = []
        self.stack_2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """

        self.stack_1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.stack_2 and not self.stack_1:
            return 0

        if not self.stack_2:
            while self.stack_1:
                self.stack_2.append(self.stack_1.pop())
            return self.stack_2.pop()
        else:
            return self.stack_2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """

        if self.stack_2:
            return self.stack_2[-1]
        else:
            if self.stack_1 and not self.stack_2:
                while self.stack_1:
                    self.stack_2.append(self.stack_1.pop())
                return self.stack_2[-1]
            else:
                return 0

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """

        if not self.stack_1 and not self.stack_2:
            return True

        return len(self.stack_1) == 0 and len(self.stack_2) == 0

    def pprint(self):
        print(self.stack_2)


if __name__ == "__main__":
    myQueue = MyQueue()
    myQueue.push(1)
    myQueue.push(2)
    print(myQueue.peek())
    print(myQueue.pop())
    print(myQueue.pop())
    myQueue.push(3)
    myQueue.push(4)
    print(myQueue.pop())
    myQueue.push(5)

    print(myQueue.empty())