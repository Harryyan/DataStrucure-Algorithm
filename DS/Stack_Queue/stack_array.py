class Stack:
    def __init__(self):
        self.__content = list()
        self.__length = 0

    def push(self, value):
        self.__content.append(value)
        self.__length += 1

    def pop(self):
        result = None
        if self.__length > 0:
            result = self.__content[self.__length - 1]
            self.__content.pop()

        self.__length -= 1
        return result

    def peek(self):
        if self.__length > 0:
            return self.__content[self.__length - 1]
        else:
            return None

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

    stack.print()
