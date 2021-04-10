
class Node:
    def __init__(self, data):
        self.data = data
        self.prior = None
        self.next = None

    def __str__(self):
        return "val:%d"%self.data if self.data else "None"


class DualList:
    def __init__(self):
        node = Node(None)
        self.head = node

    def printList(self):
        p = self.head.next

        temp = []
        while(p):
            temp.append(p.data)
            p = p.next

        print(temp)

    def insert(self, n, val):
        p = self.head
        i = 1

        while(p and i < n):
            p = p.next
            i += 1

        if not p or i > n:
            return -1

        node = Node(val)

        if p.next and i == n:
            node.next = p.next
            node.prior = p
            p.next.prior = node
            p.next = node

        if not p.next and i == n:
            node.prior = p
            p.next = node

    def delElem(self, n):
        p = self.head.next
        i = 1

        while(p and i < n):
            p = p.next
            i += 1

        if not p or i > n:
            return -1

        if p.next and i == n:
            p.prior.next = p.next
            p.next.prior = p.prior

        if not p.next and i == n:
            p.prior.next = None
            p.prior = None


if __name__ == "__main__":
    dl = DualList()

    dl.insert(1, 10)
    dl.insert(2, 20)
    dl.insert(3, 30)
    dl.insert(4, 40)
    dl.insert(5, 50)
    dl.printList()

    dl.delElem(7)
    dl.printList()