
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
        vex_map = dict(zip(self.adj_list, range(len(self.adj_list))))
        flags = [0] * len(self.adj_list)

        stack = [self.adj_list[0]]
        flags[0] = 1

        while(len(stack)):
            vex = stack.pop()
            idx = vex_map[vex]

            if isinstance(vex.data, str):
                print(vex.data, end="->")
            elif isinstance(vex.data, int):
                print(self.adj_list[vex.data].data, end="->")

            p = self.adj_list[idx]
            while p:
                if flags[p.data] == 0:
                    stack.append(p)
                    flags[p.data] = 1
                p = p.next

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


if __name__ == "__main__":
    g = Graph()
    g.createGraph(['A','B','C','D','E'], [('A','B'),('A','D'),('A','E'),('B','C'),('C','E'),('C','D'),('D','E')])
    g.printGraph()
    g.DFS()

