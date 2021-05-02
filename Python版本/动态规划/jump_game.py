
#有n块石头分别在x轴的0,1,...,n-1位置
#一只青蛙在石头0，想跳到石头n-1
#如果青蛙在第i块石头上，它最多可以向右跳距离ai
#问青蛙能否跳到石头n-1

#例子：
#输入：a=[2,3,1,1,4]
#输出：True
#输入：a=[3,2,1,0,4]
#输出：False

def jump_game(l):
    len_l = len(l)
    dp = [False] * len_l
    dp[0] = True

    for i in range(1, len_l):
        for j in range(i-1, -1, -1):
            dp[i] = dp[j] and l[j] >= i - j
            if dp[i]:
                break

    return dp[len_l - 1]


if __name__ == "__main__":
    print(jump_game([3,2,1,0,4]))