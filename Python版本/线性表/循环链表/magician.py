
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

def magician_joker():
    #初始化链表
    cl = CycleList()

    for i in range(13):
        cl.insert(i + 1, 0)

    #插牌
    p = cl.head
    for i in range(13):
        for j in range(i+1):
            p = p.next
            if p.data == None: #跳过头结点
                p = p.next

            while(p.data != 0): #如果有值，则跳过（前面的牌已被抽出）
                p = p.next

        p.data = i + 1

    cl.printList()






if __name__ == "__main__":
    magician_joker()