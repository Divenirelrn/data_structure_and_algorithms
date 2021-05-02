
#三种硬币，面值2元、5元、7元，每种硬币足够多
#买一本书需要27元
#如何用最少的硬币数正好付清，对方不用找钱

#状态：f(X)-最少用多少枚硬币拼出X

#最后的硬币ak只可能是2，5，7
#若为2，则f(27) = f(27-2) + 1
#若为5，则f(27) = f(27-5) + 1
#若为7，则f(27) = f(27-7) + 1

#则最少硬币数f(27) = min{f(27-2) + 1, f(27-5) + 1, f(27-7) + 1}

#此题可以用递归写，但重复计算太多，导致效率低下，甚至超时
#而用动态规划是将计算结果保存下来，并改变计算顺序

import sys

MAX_VALUE = sys.maxsize

def coin_change(A, M):
    f = [MAX_VALUE] * (M + 1)
    f[0] = 0

    for i in range(1, M+1):
        for j in range(len(A)):
            if i - A[j] >= 0 and f[i-A[j]] < MAX_VALUE:
                f[i] = min(f[i - A[j]] + 1, f[i])

    if f[M] == MAX_VALUE:
        f[M] = -1

    return f[M]


if __name__ == "__main__":
    print(coin_change([2, 5, 7], 27))