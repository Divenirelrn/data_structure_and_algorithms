#实现：顺序排放26个英文字母，用户输入一个数字n, 若n为正数，顺时针旋转n个;若为负数，逆时针旋转|n|个


class Node:
    def __init__(self, data):
        self.data = data
        self.prior = None
        self.next = None

    def __str__(self):
        return "val:%s"%self.data if self.data else "None"


class DualCycleList:
    def __init__(self):
        self.head = None

    def printList(self):
        p = self.head

        temp = []
        while(p.next != self.head):
            temp.append(p.data)
            p = p.next

        temp.append(p.data)
        print(temp)

    def initList(self, n):
        alp = ord('A')
        for i in range(n):
            node = Node(chr(alp))
            if not self.head:
                self.head = node
                self.head.prior = node
                node.next = self.head
                alp += 1
                continue

            self.head.prior.next = node
            node.prior = self.head.prior
            self.head.prior = node
            node.next = self.head

            alp += 1


def printLetters(dl, n):
    if n > 0:
        #顺时针旋转
        for i in range(n):
            dl.head = dl.head.next

    else:
        #逆时针旋转
        for i in range(-n):
            dl.head = dl.head.prior


if __name__ == "__main__":
    dl = DualCycleList()

    dl.initList(26)
    dl.printList()

    printLetters(dl, -3)
    dl.printList()