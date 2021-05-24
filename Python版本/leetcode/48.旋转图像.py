
def rotate(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """

    def swap(i1, j1, i2, j2):
        temp = matrix[i1][j1]
        matrix[i1][j1] = matrix[i2][j2]
        matrix[i2][j2] = temp

    n = len(matrix)
    for i in range(n):
        for j in range(n - 1 - i):
            swap(i, j, n - 1 - j, n - 1 - i)

    for i in range(n // 2):
        for j in range(n):
            swap(i, j, n - 1 - i, j)