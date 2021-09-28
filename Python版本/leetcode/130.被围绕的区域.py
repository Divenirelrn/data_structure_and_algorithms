class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        queue = collections.deque()

        def bfs():
            while len(queue):
                i, j = queue.popleft()
                board[i][j] = 'N'
                if i - 1 >= 0 and board[i - 1][j] == 'O':
                    queue.append((i - 1, j))
                if i + 1 < m and board[i + 1][j] == 'O':
                    queue.append((i + 1, j))
                if j - 1 >= 0 and board[i][j - 1] == 'O':
                    queue.append((i, j - 1))
                if j + 1 < n and board[i][j + 1] == 'O':
                    queue.append((i, j + 1))

        # Make flag of 'O' to be not replaced with 'X'
        for i in [0, m - 1]:
            for j in range(n):
                if board[i][j] == 'O':
                    queue.append((i, j))

        for j in [0, n - 1]:
            for i in range(m):
                if board[i][j] == 'O':
                    queue.append((i, j))

        bfs()

        # Replace 'O' with 'X'
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'N':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'