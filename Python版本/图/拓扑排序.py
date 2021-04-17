
class Node:
    def __init__(self, vex):
        self.data= vex
        self.next = None

class Graph:
    def __init__(self):
        self.adj_list = []

    def printGraph(self):
        for node in self.adj_list:
            print(node.data, ',', node.in_d, end="->")
            node = node.next
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

        count = [0] * len(self.adj_list)
        for vex in self.adj_list:
            p = vex.next
            while p:
                count[p.data] += 1
                p = p.next

        for vex in self.adj_list:
            vex.in_d = count[vex_dict[vex.data]]


def topological_sorting(g):
    stack = []
    for vex in g.adj_list:
        if vex.in_d == 0:
            stack.append(vex)

    count = 0
    while(len(stack)):
        vex = stack.pop()
        print(vex.data, end="->")
        count += 1

        p = vex.next
        while(p):
            g.adj_list[p.data].in_d -= 1
            if g.adj_list[p.data].in_d <= 0:
                stack.append(g.adj_list[p.data])
            p = p.next

    print("")

    if count < len(g.adj_list): #如果count < len(g.adj_list),则存在环
        return -1
    else:
        return 0





if __name__ == "__main__":
    g = Graph()
    g.createGraph([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
                  [(1,4),(1,2),(1,3),(4,8),(4,10),(4,7),(13,4),(13,14),(14,2),(14,3),
                   (14,15),(15,5),(3,10),(3,7),(3,6),(3,9),(10,11),(10,7),(11,12)])

    g.printGraph()

    print(topological_sorting(g))