
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        grids = [[None] for i in range(9)]
        rows = [[None] for i in range(9)]
        cols = [[None] for i in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                idx = (i // 3) * 3 + (j // 3)
                if board[i][j] in grids[idx] or board[i][j] in rows[i] or board[i][j] in cols[j]:
                    return False
                else:
                    grids[idx].append(board[i][j])
                    rows[i].append(board[i][j])
                    cols[j].append(board[i][j])

        return True