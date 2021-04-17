
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


def dijkstar(g, v0):
    """狄杰斯特拉算法"""
    v_len = len(g.vexs)
    parent = [v0] * v_len
    min_w = [INF] * v_len
    flags = [v0] * v_len

    for i in range(1, len(g.adjM[v0])):
        if g.adjM[v0][i] < INF:
            min_w[i] = g.adjM[v0][i]

    min_w[v0] = 0
    flags[v0] = 1

    for _ in range(1, len(g.vexs)):
        min = INF

        for i in range(len(min_w)):
            if not flags[i] and min_w[i] < min:
                min = min_w[i]
                k = i

        flags[k] = 1

        for i in range(len(g.adjM[k])):
            if not flags[i] and min + g.adjM[k][i] < min_w[i]:
                min_w[i] = min + g.adjM[k][i]
                parent[i] = k

    path = [0]
    flags = [0] * len(parent)
    flags[0] = 1
    idx = 0
    for _ in range(1, len(parent)):
        is_found = False
        for i in range(len(parent)):
            if not flags[i] and parent[i] == idx:
                path.append(i)
                idx = i
                flags[i] = 1
                is_found = True
                break

        if not is_found and idx != len(parent)-1:
            path.pop()
            idx = path[-1]

    path = [g.vexs[i] for i in path]

    return path, min_w[-1]


if __name__ == "__main__":
    g = Graph()
    g.createGraph(['v0','v1','v2','v3','v4','v5','v6','v7','v8'],
                  [('v0','v1',1),('v0','v2',5),('v1','v2',3),('v1','v3',7),('v1','v4',5),('v2','v4',1),('v2','v5',7),('v3','v4',2),
                   ('v4','v5',3),('v3','v6',3),('v4','v6',6),('v4','v7',9),('v5','v7',5),('v6','v7',2),('v6','v8',7),('v7','v8',4)])
    print(g.vexs)
    print("--------------------------------------------------------------")
    for i in range(len(g.adjM)):
        for j in range(len(g.adjM[0])):
            print("%-6d"%g.adjM[i][j], end=" ")
        print("\n")
    print("--------------------------------------------------------------")

    print(dijkstar(g, 0))