
from collections import deque

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
            self.adjM.append([0] * num_vex)

        for edge in edges:
            i, j = vex_index[edge[0]], vex_index[edge[1]]

            self.adjM[i][j] = 1
            self.adjM[j][i] = 1

    def DFS(self):
        """深度优先遍历非递归（栈）"""
        vex_map = dict(zip(self.vexs, range(len(self.vexs))))
        flags = [0] * len(self.vexs)

        stack = [self.vexs[0]]
        flags[0] = 1

        while(len(stack)):
            vex = stack.pop()
            idx = vex_map[vex]
            print(vex, end="->")

            #找到vex的相邻顶点
            for i in range(len(self.adjM[idx])):
                if self.adjM[idx][i] == 1 and flags[i] == 0:
                    stack.append(self.vexs[i])
                    flags[i] = 1

    def dfs(graph):
        """深度优先遍历递归"""
        vex_dict = dict(zip(graph.vexs, range(len(graph.vexs))))
        flags = [0] * len(vex_dict)

        def dfs_in(vex):
            print(vex, end="->")
            idx = vex_dict[vex]
            flags[idx] = 1

            adj_m = graph.adjM[idx]
            for i in range(len(adj_m)):
                if adj_m[i] == 1 and flags[i] == 0:
                    dfs_in(graph.vexs[i])
                    flags[i] = 1

        dfs_in(graph.vexs[0])

        del vex_dict
        del flags

    def BFS(self):
        """广度优先遍历非递归（队列）"""
        vex_map = dict(zip(self.vexs, range(len(self.vexs))))
        flags = [0] * len(self.vexs)

        q = deque()
        q.append(self.vexs[0])
        flags[0] = 1

        while(len(q)):
            vex = q.popleft()
            idx = vex_map[vex]
            print(vex, end="->")

            for i in range(len(self.adjM[idx])):
                if self.adjM[idx][i] == 1 and flags[i] == 0:
                    q.append(self.vexs[i])
                    flags[i] = 1

        del vex_map
        del flags

    def is_circle(g):
        """判断图中是否有环"""
        vex_map = dict(zip(g.vexs, range(len(g.vexs))))
        flags = [0] * len(g.vexs)

        stack = [g.vexs[0]]
        flags[0] = 1
        p = None

        while (len(stack)):
            vex = stack.pop()
            idx = vex_map[vex]

            for i in range(len(g.adjM[idx])):
                if g.adjM[idx][i] == 1:
                    if flags[i] == 0:
                        stack.append(g.vexs[i])
                        flags[i] = 1
                        p = g.vexs[i]

                    if flags[i] == 1 and g.vexs[i] != p:
                        return True

            p = vex

        return False


if __name__ == "__main__":
    g = Graph()
    g.createGraph(['A','B','C','D','E'], [('A','B'),('A','D'),('A','E'),('B','C'),('C','E'),('C','D'),('D','E')])
    print(g.vexs)
    for i in g.adjM:
        print(i)

    # g.DFS()
    g.BFS()


