#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param str string字符串
# @return string字符串一维数组
#
class Solution:
    def Permutation(self, str: str) -> List[str]:
        # write code here
        str = sorted(str)
        n = len(str)
        ans = list()
        visited = [0] * n

        def dfs(idx, temp):
            if idx == n:
                ans.append("".join(temp))
                return

            for i in range(n):
                if visited[i] or (i > 0 and str[i] == str[i - 1] and not visited[i - 1]):
                    continue
                temp.append(str[i])
                visited[i] = 1
                dfs(idx + 1, temp)
                visited[i] = 0
                temp.pop()

        dfs(0, list())
        return ans