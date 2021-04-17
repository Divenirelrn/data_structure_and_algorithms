
INF = 65535

class Graph:
    def __init__(self):
        self.vexs = []
        self.adjM = []

    def createGraph(self, vexs, edges):
        self.vexs = vexs

        #建立顶点下标映射表
        num_vex = len(vexs)
        vex_index = dict(zip(vexs, range(num_vex)))

        #邻接矩阵初始化
        for i in range(num_vex):
            self.adjM.append([INF] * num_vex)

        for i in range(num_vex):
            self.adjM[i][i] = 0

        for edge in edges:
            v1, v2, w = edge
            i, j = vex_index[v1], vex_index[v2]

            self.adjM[i][j] = w
            self.adjM[j][i] = w


def is_circle(g):
    vex_map = dict(zip(g.vexs, range(len(g.vexs))))
    flags = [0] * len(g.vexs)
    pre_map = dict()

    stack = [g.vexs[0]]
    flags[0] = 1
    pre_map[g.vexs[0]] = None

    while (len(stack)):
        vex = stack.pop()
        idx = vex_map[vex]

        for i in range(len(g.adjM[idx])):
            if i == idx:
                continue

            if g.adjM[idx][i] < INF:
                if flags[i] == 1 and g.vexs[i] != pre_map[vex] and pre_map[vex] != None:
                    return True

                if flags[i] == 0:
                    stack.append(g.vexs[i])
                    flags[i] = 1
                    pre_map[g.vexs[i]] = vex

    return False


def kruscal(g):
    # 边与权值映射表
    edge_map = {}
    for i in range(len(g.adjM)):
        for j in range(i + 1, len(g.adjM[0])):
            if g.adjM[i][j] < INF:
                edge_map[(i, j)] = g.adjM[i][j]

    edge_map = sorted(edge_map.items(), key=lambda x: x[1])

    # 初始化新图
    g_new = Graph()
    g_new.vexs = g.vexs
    g_new.adjM = g.adjM

    for i in range(len(g_new.adjM)):
        for j in range(len(g_new.adjM[0])):
            if i == j:
                continue

            if g_new.adjM[i][j] != INF:
                g_new.adjM[i][j] = INF

    g_tree = []
    for edge in edge_map:
        (i, j), w = edge
        g_new.adjM[i][j] = w
        g_new.adjM[j][i] = w

        flag = is_circle(g_new)
        if not flag:
            g_tree.append((g.vexs[i], g.vexs[j]))

            if len(g_tree) >= len(g_new.vexs) - 1:
                break
        else:
            g_new.adjM[i][j] = INF
            g_new.adjM[j][i] = INF

    del edge_map
    del g_new

    return g_tree


def prim(g):
    vex_map = dict(zip(g.vexs, range(len(g.vexs))))

    selected = [False] * len(g.vexs)
    minEdge = [INF] * len(g.vexs)
    parent = [-1] * len(g.vexs)

    idx = 0
    selected[0] = True
    minEdge[0] = None
    while(sum(selected) < len(g.vexs)):
        for i in range(len(g.adjM[idx])):
            if i == idx:
                continue

            if g.adjM[idx][i] < INF and not selected[i] and g.adjM[idx][i] < minEdge[i]:
                minEdge[i] = g.adjM[idx][i]
                parent[i] = idx #bug

        min = INF
        for i in range(len(minEdge)):
            if minEdge[i] == None:
                continue

            if minEdge[i] < min:
                min = minEdge[i]
                idx = i

        selected[idx] = True
        minEdge[idx] = None

    mTree = []
    for i in range(len(parent)):
        if parent[i] != -1:
            mTree.append((g.vexs[i], g.vexs[parent[i]]))

    del selected
    del minEdge
    del parent
    del vex_map

    return mTree


if __name__ == "__main__":
    g = Graph()
    # g.createGraph(['A','B','C','D','E'], [('A','B',12),('A','D',1),('A','E',5),('B','C',6),('C','E',8),('C','D',10),('D','E', 6)])
    g.createGraph([0,1,2,3,4,5,6,7,8], [(0,1,4),(0,7,8),(1,7,11),(1,2,8),(7,8,7),(7,6,1),(2,8,2),(8,6,6),(2,3,7),(2,5,4),(6,5,2),(3,5,14),(3,4,9),(5,4,10)])
    print(g.vexs)
    for i in g.adjM:
        print(i)

    # print(is_circle(g))

    # print("kruscal:", kruscal(g))
    print("prim:", prim(g))



