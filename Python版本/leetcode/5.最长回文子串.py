
#方法一：动态规划
class Solution:
    def longestPalindrome(self, s: str) -> str:
        #动态规划
        len_s = len(s)
        dp = [[False]*len_s for _ in range(len_s)]

        for i in range(len_s):
            dp[i][i] = True

        max_l = 1
        l = 0
        for j in range(len_s):
            for i in range(j):
                if j - i == 1:
                    dp[i][j] = s[i] == s[j]
                elif i < len_s - 1 and j > 0:
                    dp[i][j] = dp[i+1][j-1] and s[i] == s[j]

                if dp[i][j] and j - i + 1 > max_l:
                    max_l = j - i + 1
                    l = i

        return s[l : l + max_l]


#方法二：中心扩散
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def c_expand(i, j):
            while(i >= 0 and j < len_s and s[i] == s[j]):
                i -= 1
                j += 1

            return i+1, j-1

        len_s = len(s)
        l = r = 0
        for i in range(len_s):
            l1, r1 = c_expand(i, i)
            l2, r2 = c_expand(i, i+1)

            if r1 - l1 > r - l:
                l, r = l1, r1
            if r2 - l2 > r - l:
                l, r = l2, r2

        return s[l:r+1]