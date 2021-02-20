class Stack:
    def __init__(self):
        self.content = []

    def push(self, value):
        self.content.insert(0, value)

    def pop(self):
        result = None
        if len(self.content) > 0:
            result = self.content[0]
            self.content.pop(0)

        return result

    def peek(self):
        if len(self.content) > 0:
            return self.content[0]
        else:
            return None

    def print(self):
        for item in self.content:
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
