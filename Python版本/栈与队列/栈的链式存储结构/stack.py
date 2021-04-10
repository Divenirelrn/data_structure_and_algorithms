
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class LinkedStack:
    def __init__(self):
        self.top = Node(None)

    def push(self, val):
        node = Node(val)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.top.data == None:
            return -1

        temp = self.top.data
        p = self.top
        self.top = self.top.next
        del p

        return temp


if __name__ == "__main__":
    ls = LinkedStack()
    ls.push(10)
    ls.push(20)
    ls.push(30)
    ls.push(40)

    print(ls.pop())
    print(ls.pop())
    print(ls.pop())
    print(ls.pop())
    print(ls.pop())