
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        len_w = len(word)
        fir_letters = []
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    fir_letters.append([i, j])

        if len_w == 1:
            return bool(len(fir_letters))

        def dfs(fir_letter):
            s = [[fir_letter]]
            while len(s):
                ids = s.pop()
                i, j = ids[-1]
                idx = len(ids)
                if idx == len_w:
                    return True
                if i >= 1 and board[i-1][j] == word[idx] and [i-1, j] not in ids:
                    s.append(ids + [[i-1, j]])
                if i < m - 1 and board[i+1][j] == word[idx] and [i+1, j] not in ids:
                    s.append(ids + [[i+1, j]])
                if j >= 1 and board[i][j-1] == word[idx] and [i, j-1] not in ids:
                    s.append(ids + [[i, j-1]])
                if j < n - 1 and board[i][j+1] == word[idx] and [i, j+1] not in ids:
                    s.append(ids + [[i, j+1]])

            return False


        for fir_letter in fir_letters:
            if dfs(fir_letter):
                return True

        return False