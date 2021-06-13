
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 1:
            return [[1]]

        #0-row, 1-col
        direct = 1
        #0-sub, 1-add
        flag = 1

        ans = [[None] * n for _ in range(n)]
        value = 1
        i = j = 0
        while value <= n * n:
            #col
            if direct == 1:
                #col add
                if flag == 1 and j < n - i:
                    ans[i][j] = value
                    j += 1
                    if j >= n - i:
                        direct = 0
                        flag = 1
                        j -= 1
                        i += 1
                #col sub
                elif flag == 0 and j > n - i - 2:
                    ans[i][j] = value
                    j -= 1
                    if j <= n -i - 2:
                        direct = 0
                        flag = 0
                        j += 1
                        i -= 1
            #row
            else:
                #row add
                if flag == 1 and i < 1 + j:
                    ans[i][j] = value
                    i += 1
                    if i >= 1 + j:
                        direct = 1
                        flag = 0
                        i -= 1
                        j -= 1
                #row sub
                elif flag == 0 and i > j:
                    ans[i][j] = value
                    i -= 1
                    if i <= j:
                        direct = 1
                        flag = 1
                        i += 1
                        j += 1

            value += 1

        return ans