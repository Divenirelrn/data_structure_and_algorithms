#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param grid int整型二维数组
# @return int整型
#
class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        # write code here
        m, n = len(grid), len(grid[0])
        for i in range(1, n):
            grid[0][i] += grid[0][i - 1]
        for j in range(1, m):
            grid[j][0] += grid[j - 1][0]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = max(grid[i][j - 1] + grid[i][j], grid[i - 1][j] + grid[i][j])

        return grid[-1][-1]