class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        if m == 0:
            return 0

        def bfs(i, j):
            queue = collections.deque()
            queue.append((i, j))
            grid[i][j] = "0"

            while len(queue):
                i, j = queue.popleft()

                #down
                if i + 1 < m and grid[i+1][j] == "1":
                    queue.append((i+1, j))
                    grid[i+1][j] = "0"
                #up
                if i - 1 >= 0 and grid[i-1][j] == "1":
                    queue.append((i-1, j))
                    grid[i-1][j] = "0"
                #right
                if j + 1 < n and grid[i][j+1] == "1":
                    queue.append((i, j+1))
                    grid[i][j+1] = "0"
                #left
                if j - 1 >= 0 and grid[i][j-1] == "1":
                    queue.append((i, j-1))
                    grid[i][j-1] = "0"


        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    bfs(i, j)
                    count += 1

        return count