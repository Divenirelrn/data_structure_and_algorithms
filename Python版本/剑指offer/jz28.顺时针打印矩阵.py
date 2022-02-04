#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param matrix int整型二维数组
# @return int整型一维数组
#
class Solution:
    def printMatrix(self, matrix: List[List[int]]) -> List[int]:
        # write code here
        m, n = len(matrix), len(matrix[0])
        if m == 0 or n == 0:
            return list()

        total = m * n
        row, col = 0, 0
        visited = [[False] * n for _ in range(m)]
        res = [0] * total
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        idx = 0

        for i in range(total):
            res[i] = matrix[row][col]
            visited[row][col] = True

            nextRow, nextCol = row + direction[idx][0], col + direction[idx][1]
            if not (nextRow >= 0 and nextRow < m and nextCol >= 0 and nextCol < n \
                    and not visited[nextRow][nextCol]):
                idx = (idx + 1) % 4

            row = row + direction[idx][0]
            col = col + direction[idx][1]

        return res