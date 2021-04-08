import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return "Node value: %d"%self.data

    def __del__(self):
        print("delete")

class LinkedList:
    def __init__(self):
        head_node = Node(None)
        self.head = head_node

    def is_empty(self):
        return self.head.next == None

    def printList(self):
        temp = []
        p = self.head.next
        while p != None:
            temp.append(p.data)
            p = p.next
        print(temp)

    def insert(self, idx, data):
        p = self.head
        i = 1
        while(p and i < idx):
            p = p.next
            i += 1

        if not p or i > idx:
            return -1

        node = Node(data)
        node.next = p.next
        p.next = node

        return 0

    def getElem(self, idx):
        i = 1
        p = self.head.next

        while(p and i < idx):
            p = p.next
            i += 1

        if not p or i > idx:
            return -1

        return p.data

    def deleteElem(self, idx):
        i, p = 1, self.head

        while(p.next and i < idx):
            p = p.next
            i += 1

        if not p.next or i > idx:
            return -1

        delElem = p.next
        p.next = p.next.next

        return delElem

    def init_list_head(self, n):
        p = self.head
        for i in range(n):
            node = Node(random.randint(1,10))
            node.next = p.next
            p.next = node

    def init_list_tail(self, n):
        p = self.head

        for i in range(n):
            node = Node(i)
            p.next = node
            p = p.next

    def destroy_list(self):
        p = self.head.next

        while(p):
            q = p.next
            del p
            p = q

        self.head.next = None


if __name__ == "__main__":
    l = LinkedList()

    l.init_list_tail(5)
    l.printList()

    l.destroy_list()
    # l.printList()
    # l.insert(0, 20)
    # l.insert(1, 20)
    # l.insert(2, 30)
    # l.insert(3, 40)
    # l.insert(4, 50)
    # l.insert(5, 60)
    # l.printList()
    #
    # print(l.getElem(7))
    #
    # print(l.deleteElem(8))
    # l.printList()



