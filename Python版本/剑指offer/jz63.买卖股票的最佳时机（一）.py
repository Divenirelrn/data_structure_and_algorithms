#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param prices int整型一维数组
# @return int整型
#
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # write code here
        n = len(prices)
        if n <= 1:
            return 0
        minValue = prices[0]
        curProfit = 0
        res = 0
        for i in range(1, n):
            if prices[i] < minValue:
                minValue = prices[i]
                curProfit = 0
            else:
                curProfit = prices[i] - minValue

            res = max(res, curProfit)

        return res

