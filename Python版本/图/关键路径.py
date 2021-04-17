
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
                print(node.data,',',node.weight, end="->")
                node = node.next
            print("")

    def createGraph(self, vexs, edges):
        #建立映射表
        vex_dict = dict(zip(vexs, range(len(vexs))))

        for vex in vexs:
            node = Node(vex)
            self.adj_list.append(node)

        for edge in edges:
            i, j, w = vex_dict[edge[0]], vex_dict[edge[1]], edge[2]

            node = Node(j)
            node.weight = w
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

def topological_sorting(g, vex_map):
    stack = []
    stack2 = []
    etv = [0] * len(g.adj_list)
    for vex in g.adj_list:
        if vex.in_d == 0:
            stack.append(vex)

    count = 0
    while(len(stack)):
        vex = stack.pop()
        stack2.append(vex)
        count += 1

        p = vex.next
        while(p):
            g.adj_list[p.data].in_d -= 1
            if g.adj_list[p.data].in_d <= 0:
                stack.append(g.adj_list[p.data])

            if p.weight + etv[vex_map[vex]] > etv[p.data]:
                etv[p.data] = p.weight + etv[vex_map[vex]]

            p = p.next

    if count < len(g.adj_list): #如果count < len(g.adj_list),则存在环
        return -1
    else:
        return stack2, etv

def printStack(s):
    while(len(s)):
        v = s.pop()
        print(v.data, end=" ")
    print("")

def crutial_path(g):
    vex_map = dict(zip(g.adj_list, range(len(g.adj_list))))

    stack2, etv = topological_sorting(g, vex_map)
    ltv = [etv[-1]] * len(g.adj_list)

    while(len(stack2)):
        vex = stack2.pop()

        p = vex.next
        while(p):
            if ltv[p.data] - p.weight < ltv[vex_map[vex]]:
                ltv[vex_map[vex]] = ltv[p.data] - p.weight
            p = p.next

    for i in range(len(etv)):
        vex = g.adj_list[i]
        p = vex.next

        while p:
            ete = etv[vex_map[vex]]
            lte = ltv[p.data] - p.weight

            if ete == lte:
                print("<%d, %d>, %d"%(vex.data, g.adj_list[p.data].data, p.weight), end='    ')

            p = p.next







if __name__ == "__main__":
    g = Graph()
    g.createGraph([1,2,3,4,5,6,7,8,9],[(1,2,6),(1,3,4),(1,4,5),(2,5,1),
                (3,5,1),(4,6,2),(5,7,7),(5,8,5),(6,8,4),(7,9,2),(8,9,4)])

    # g.printGraph()

    crutial_path(g)