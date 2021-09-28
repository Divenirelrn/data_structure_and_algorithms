
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)

        dp = [[True] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                dp[i][j] = s[i] == s[j] and dp[i+1][j-1]

        def inner(i):
            if i == n:
                ans.append(temp[:])
                return

            for j in range(i, n):
                if dp[i][j]:
                    temp.append(s[i:j+1])
                    inner(j+1)
                    temp.pop()


        temp = []
        ans = []
        inner(0)

        return ans