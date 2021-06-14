
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        MAXSIZE = 65536

        m = len(grid)
        n = len(grid[0])

        dp = [MAXSIZE] * n
        dp[0] = grid[0][0]

        for i in range(m):
            for j in range(n):
                if i == 0 and j >= 1:
                    dp[j] = dp[j - 1] + grid[i][j]
                elif j == 0 and i >= 1:
                    dp[j] = dp[j] + grid[i][j]
                elif i >= 1 and j >= 1:
                    dp[j] = min(dp[j-1] + grid[i][j], dp[j] + grid[i][j])

        return dp[-1]
