
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)

        dp = [0] * (n+1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i-1, -1, -1):
                dp[i] = dp[j] and s[j:i] in wordSet
                if dp[i]:
                    break

        return dp[n]