
class Stack:
    def __init__(self):
        self.c = []
        self.base = self.top = None

    def printStack(self):
        print(self.c)

    def push(self, val):
        if not len(self.c):
            self.c.append(val)
            self.base = self.top = self.c[0]
            return 0

        self.c.append(val)
        self.top = self.c[-1]
        return 0

    def pop(self):
        if not len(self.c):
            return -1

        temp = self.c[-1]
        if len(self.c)== 1:
            self.top = self.base = None
        else:
            self.top = self.c[-2]
        self.c.pop()
        return temp


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)

    s.printStack()

    s.pop()
    s.pop()
    s.pop()
    s.printStack()
