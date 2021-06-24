
class Solution:
    def grayCode(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        dp[0] = ["0"]
        dp[1] = ["0", "1"]

        for i in range(2, n+1):
            pre = ['0' + text for text in dp[i-1]]
            post = ['1' + dp[i-1][j] for j in range(len(dp[i-1])-1, -1, -1)]
            dp[i] = pre + post

        return [int(text, 2) for text in dp[n]]