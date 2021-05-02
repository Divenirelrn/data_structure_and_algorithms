
#任务1：1点到4点，5元
#任务2：3点到5点，1元
#任务3：0点到6点，8元
#任务4：4点到7点，4元
#任务5：3点到8点，6元
#任务6：5点到9点，3元
#任务7：6点到10点，2元
#任务8：8点到11点，4元

#求选择哪几个能得到最大收益

#dp[i] = max{dp[i-1], dp[i-x] + a[i]}
def max_profit(l):
    len_l = len(l)
    dp = [0] * len_l
    dp[0] = l[0][1]

    for i in range(1, len_l):
        j = i - 1
        while j >= 0:
            if l[j][0][1] <= l[i][0][0] or l[j][0][0] >= l[i][0][1]:
                break
            j -= 1

        if j >= 0:
            dp[i] = max(dp[i-1], l[i][1] + dp[j])
        else:
            dp[i] = max(dp[i - 1], l[i][1])

    return dp[len_l - 1]


if __name__ == "__main__":
    print(max_profit([((1, 4), 5), ((3, 5), 1), ((0, 6), 8), ((4, 7), 4),
                      ((3, 8), 6), ((5, 9), 3), ((6, 10), 2), ((8, 11), 4)]))