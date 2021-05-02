
#给定m行n列的网格，一个机器人从左上角(0,0)出发，每一步可向下或向右走一步
#问有多少种方式可以走到右下角

#dp[i][j] = dp[i-1][j] + dp[i][j-1]

def unique_paths(m ,n):
    dp = [[0] * n for _ in range(m)]
    for j in range(n):
        dp[0][j] = 1

    for i in range(1, m):
        dp[i][0] = 1

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[m-1][n-1]


if __name__ == "__main__":
    print(unique_paths(4, 8))