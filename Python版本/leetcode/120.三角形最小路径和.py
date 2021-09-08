
class Solution:
    def minimumTotal(self, triangle) -> int:
        n = len(triangle)
        if n == 1:
            return triangle[0][0]

        dp = [0] * n
        dp[0] = [triangle[0][0]]

        for i in range(1, n):
            dp[i] = []
            for j in range(len(triangle[i])):
                if j == 0:
                    dp[i].append(dp[i-1][0] + triangle[i][0])
                elif j == len(triangle[i]) - 1:
                    dp[i].append(dp[i-1][-1] + triangle[i][-1])
                else:
                    dp[i].append(min(dp[i-1][j-1] + triangle[i][j], dp[i-1][j] + triangle[i][j]))

        min_val = dp[-1][0]
        for i in range(1, len(dp[-1])):
            if dp[-1][i] < min_val:
                min_val = dp[-1][i]

        return min_val


if __name__ == "__main__":
    s = Solution()
    print(s.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))