class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        if m * n == 1:
            return [matrix[0][0]]

        #0-row, 1-col
        direct = 1
        #0-sub, 1-add
        flag = 1

        ans = []
        i = j = 0
        while len(ans) < m * n:
            #col
            if direct == 1:
                #col add
                if flag == 1 and j < n - i:
                    ans.append(matrix[i][j])
                    j += 1
                    if j >= n - i:
                        direct = 0
                        flag = 1
                        j -= 1
                        i += 1
                #col sub
                elif flag == 0 and j > m - i - 2:
                    ans.append(matrix[i][j])
                    j -= 1
                    if j <= m -i - 2:
                        direct = 0
                        flag = 0
                        j += 1
                        i -= 1
            #row
            elif direct == 0:
                #row add
                if flag == 1 and i < m - n + 1 + j:
                    ans.append(matrix[i][j])
                    i += 1
                    if i >= m - n + 1 + j:
                        direct = 1
                        flag = 0
                        i -= 1
                        j -= 1
                #row sub
                elif flag == 0 and i > j:
                    ans.append(matrix[i][j])
                    i -= 1
                    if i <= j:
                        direct = 1
                        flag = 1
                        i += 1
                        j += 1

        return ans