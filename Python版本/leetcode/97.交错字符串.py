
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)
        len_s3 = len(s3)

        if len_s1 + len_s2 != len_s3:
            return False

        dp = [[False] * (len_s2 + 1) for j in range(len_s1 + 1)]

        for i in range(0, len_s1 + 1):
            for j in range(0, len_s2 + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = True if s2[j - 1] == s3[i + j - 1] and dp[i][j - 1] else False
                elif j == 0:
                    dp[i][j] = True if s1[i - 1] == s3[i + j - 1] and dp[i - 1][j] else False
                else:
                    if s1[i - 1] == s3[i + j - 1] and dp[i - 1][j] or s2[j - 1] == s3[i + j - 1] and dp[i][j - 1]:
                        dp[i][j] = True

        return dp[-1][-1]



