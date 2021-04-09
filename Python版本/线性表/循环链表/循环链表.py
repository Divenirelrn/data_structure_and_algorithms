
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

    def __str__(self):
        text = ("val:%d"%self.data) if self.data else "None"
        return text

class CycleList:
    def __init__(self):
        self.head = Node(None)
        self.head.next = self.head

    def printList(self):
        p = self.head
        node_list = []
        while(p.next != self.head):
            p = p.next
            node_list.append(p.data)

        print(node_list)

    def insert(self, idx, val):
        p = self.head
        i = 1

        while(p.next != self.head and i < idx):
            p = p.next
            i += 1

        if i != idx:
            return -1

        node = Node(val)
        if p.next == self.head:
            node.next = self.head
            p.next = node
        elif i == idx:
            node.next = p.next
            p.next = node

        return 0

    def search(self, idx):
        if self.head.next == self.head or idx < 1:
            return -1

        p = self.head.next
        i = 1

        while(p.next != self.head and i < idx):
            p = p.next
            i += 1

        if i < idx:
            return -1

        return p.data

    def delElem(self, idx):
        if not self.head.next or idx < 1:
            return -1

        p = self.head
        i = 1

        while(p.next != self.head and i < idx):
            p = p.next
            i += 1

        if p.next == self.head and i <= idx:
            return -1

        if p.next.next == self.head and i == idx:
            p.next = self.head

        if p.next != self.head and i == idx:
            p.next = p.next.next

        return 0


if __name__ == "__main__":
    cl = CycleList()

    print(cl.insert(0, 10))
    print(cl.insert(1, 10))
    print(cl.insert(2, 20))
    print(cl.insert(3, 30))
    print(cl.insert(4, 40))
    print(cl.insert(5, 50))
    print(cl.insert(6, 100))
    cl.printList()

    print(cl.search(8))

    print(cl.delElem(1))
    cl.printList()