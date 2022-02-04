#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param matrix char字符型二维数组
# @param word string字符串
# @return bool布尔型
#
class Solution:
    def hasPath(self, matrix, word):
        # write code here
        m, n = len(matrix), len(matrix[0])
        lenStr = len(word)

        def dfs(i, j, idx):
            if matrix[i][j] != word[idx]:
                return False

            if idx == lenStr - 1:
                return True

            result = False
            visited.add((i, j))
            for ii, jj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if ii >= 0 and ii < m and jj >= 0 and jj < n and (ii, jj) not in visited:
                    if dfs(ii, jj, idx + 1):
                        result = True
                        break
            visited.remove((i, j))

            return result

        visited = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == word[0] and dfs(i, j, 0):
                    return True

        return False