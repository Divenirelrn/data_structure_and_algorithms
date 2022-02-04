# -*- coding:utf-8 -*-
class Solution:
    def cutRope(self, number):
        # write code here
        dp = [0] * number
        dp[0] = 1

        for i in range(1, number):
            maxValue = 0
            for j in range(i - 1, -1, -1):
                maxValue = max(maxValue, dp[j] * (i - j), (j + 1) * (i - j))

            dp[i] = maxValue

        return dp[-1]


#方法二：递归
# -*- coding:utf-8 -*-
class Solution:
    def cutRope(self, number):
        # write code here
        def maxValue(n):
            if n <= 4:
                return n

            if cache.get(n, None):
                return cache[n]

            res = 0
            for i in range(1, n):
                res = max(res, i * maxValue(n - i))

            cache[n] = res
            return res

        if number == 2:
            return 1
        elif number == 3:
            return 2

        cache = dict()
        return maxValue(number)