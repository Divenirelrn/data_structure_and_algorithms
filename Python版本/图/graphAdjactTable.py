
from collections import deque

class Node:
    def __init__(self, vex):
        self.data= vex
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

    def createGraph(self, vexs, edges):
        #建立映射表
        vex_dict = dict(zip(vexs, range(len(vexs))))

        for vex in vexs:
            node = Node(vex)
            self.adj_list.append(node)

        for edge in edges:
            i, j = vex_dict[edge[0]], vex_dict[edge[1]]

            node = Node(j)
            node.next = self.adj_list[i].next
            self.adj_list[i].next = node

            node = Node(i)
            node.next = self.adj_list[j].next
            self.adj_list[j].next = node

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

    def dfs(graph):
        """深度优先遍历递归"""
        for vex in graph.adj_list:
            vex.flag = 0

        def dfs_in(vex):
            print(vex.data, end="->")
            vex.flag = 1

            p = vex.next
            while p:
                vex = graph.adj_list[p.data]
                if vex.flag == 0:
                    dfs_in(vex)
                p = p.next

        dfs_in(graph.adj_list[0])

        for vex in graph.adj_list:
            delattr(vex, "flag")

    def BFS(self):
        """广度优先遍历非递归（队列）"""
        for vex in self.adj_list:
            vex.flag = 0

        q = deque()
        q.append(self.adj_list[0])
        self.adj_list[0].flag = 1

        while(len(q)):
            vex = q.popleft()
            print(vex.data, end="->")

            p = vex.next
            while(p):
                vex = self.adj_list[p.data]
                if vex.flag == 0:
                    q.append(vex)
                    vex.flag = 1

                p = p.next





if __name__ == "__main__":
    g = Graph()
    g.createGraph(['A','B','C','D','E'], [('A','B'),('A','D'),('A','E'),('B','C'),('C','E'),('C','D'),('D','E')])
    g.printGraph()
    g.DFS()
    print("\n")
    g.BFS()

