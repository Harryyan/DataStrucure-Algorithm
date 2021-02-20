class Stack:
    # 需要考虑时间复杂度，对于顺序表, 操作尾部是O(1)的复杂度
    # 对于链表，则要操作头部
    # 对于 python: 0, {}, [] 返回 false
    def __init__(self):
        self.__content = list()

    def push(self, value):
        self.__content.append(value)

    def pop(self):
        result = None
        if self.__content:
            restul = self.__content.pop()

        return result

    def peek(self):
        if self.__content:
            return self.__content[-1]
        else:
            return None

    def is_empty(self):
        return not self.__content

    def print(self):
        for item in reversed(self.__content):
            print(item, end=" ")
        print("\n")


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)

    stack.print()

    stack.pop()
    stack.pop()
    stack.pop()

    print(stack.peek())
