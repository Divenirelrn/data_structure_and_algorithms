

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

    def __str__(self):
        text = ("val:%d"%self.data) if self.data!=None else "None"
        return text

class CycleList:
    def __init__(self):
        self.head = None

    def printList(self):
        p = self.head
        node_list = []
        while(p.next != self.head):
            node_list.append(p.data)
            p = p.next

        node_list.append(p.data)
        print(node_list)

    def initList(self, n):
        for i in range(n):
            node = Node(i+1)
            if not self.head:
                node.next = node
                self.head = node
                continue

            p = self.head

            while p.next != self.head:
                p = p.next

            node.next = self.head
            p.next = node

def josphus(n, i):
    cl = CycleList()
    cl.initList(n)

    flag = [0] * n
    count = 0

    p = cl.head
    j = 1

    while True:
        if j > i:
            j = 1

        if j == i:
            print(p.data)
            flag[p.data-1] = 1
            count += 1
            if count >= n:
                break

        while True:
            p = p.next
            if not flag[p.data-1]:
                break
        j += 1


if __name__ == "__main__":
    josphus(41, 3)