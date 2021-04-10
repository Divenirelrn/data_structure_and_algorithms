import random
random.seed(0)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return "Node value: %d"%self.data

class LinkedList:
    def __init__(self):
        head_node = Node(None)
        self.head = head_node

    def printList(self):
        temp = []
        p = self.head.next
        while p != None:
            temp.append(p.data)
            p = p.next
        print(temp)

    def init_list_tail(self, n, loc=None):
        p = self.head

        for i in range(n):
            node = Node(i + 1)
            p.next = node
            p = p.next

        if loc:
            q = self.head.next
            i = 1

            while(q and i < loc):
                q = q.next
                i += 1

            p.next = q
            print(p)
            print(p.next)

def is_looped(l):
    """
    快慢指针
    """
    s = f = l.head

    while(True):
        s = s.next
        f = f.next.next

        if s == f or not f:
            break

    if s == f:
        return True

    if not f:
        return False

def is_looped2(l):
    """
    双指针
    """
    p = l.head
    i = 1

    while p:
        p = p.next
        i += 1

        q = l.head
        j = 1

        while(q != p):
            q = q.next
            j += 1

        if i != j:
            break

    if not p:
        return False

    if i != j:
        return True


if __name__ == "__main__":
    l = LinkedList()

    l.init_list_tail(10, 3)
    # l.printList()
    print(is_looped2(l))

