
#方法一：迭代（超时）
class Solution:
    def numTrees(self, n: int) -> int:
        def inner(start, end):
            if start >= end:
                return 1

            total = 0
            for i in range(start, end+1):
                count_l = inner(start, i-1)
                count_r = inner(i + 1, end)

                total += count_l * count_r

            return total

        total = inner(1, n)
        return total if n else 0

#方法二：动态规划
"""
G(n) - 长度为n的序列组成的不同二叉搜索树个数
F(i, n) - 以i为根节点，长度为n的序列组成的二叉搜索树个数
则 G(n) = \sum_{i=1}^{n}{F(i, n)}
而F(i, n) = G(i-1) * G(n - i)
则G(n) = \sum_{i=1}^{n}{G(i-1)*G(n-i)}
"""
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]

        return dp[-1]

