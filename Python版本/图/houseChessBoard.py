"""
马踏棋盘算法（骑士周游问题）
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Graph:
    def __init__(self):
        self.adj_list = []

    def printGraph(self):
        for node in self.adj_list:
            while node:
                print(node.data, end="->")
                node = node.next
            print("\n")

    def DFS(self):
        """深度优先遍历非递归（栈）"""
        for node in self.adj_list:
            node.flag = 0

        stack = [self.adj_list[0]]
        self.adj_list[0].flag = 1

        while (len(stack)):
            vex = stack.pop()
            print(vex.data, end="->")

            p = vex.next
            while p:
                node = self.adj_list[p.data]
                if node.flag == 0:
                    stack.append(node)
                    node.flag = 1
                p = p.next

        for node in self.adj_list:
            delattr(node, "flag")

def houseChessBoard(n):
    g = Graph()
    for i in range(n * n):
        node = Node(i)
        g.adj_list.append(node)

    def append_node(idx, i, j):
        node = Node(i * n + j)
        node.next = g.adj_list[idx].next
        g.adj_list[idx].next = node

    for i in range(n):
        for j in range(n):
            idx = i * n + j
            if i >= 1:
                if j >= 2:
                    append_node(idx, i-1, j-2)
                if j <= n-3:
                    append_node(idx, i-1, j+2)
            if i >= 2:
                if j >= 1:
                    append_node(idx, i-2, j-1)
                if j <= n-2:
                    append_node(idx, i-2, j+1)
            if i <= n - 2:
                if j >= 2:
                    append_node(idx, i+1, j-2)
                if j <= n-3:
                    append_node(idx, i+1, j+2)
            if i <= n - 3:
                if j <= n-2:
                    append_node(idx, i+2, j+1)
                if j >= 1:
                    append_node(idx, i+2, j-1)

    # g.printGraph()
    g.DFS()


if __name__ == "__main__":
    houseChessBoard(8)

