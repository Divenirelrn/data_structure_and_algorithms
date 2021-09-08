class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0

        profits = [0] * n
        min_idx = 0
        for i in range(1, n):
            if prices[i] > prices[min_idx]:
                profits[i] = prices[i] - prices[min_idx]
            else:
                min_idx = i

        max_pro = 0
        for i in range(n):
            if profits[i] > max_pro:
                max_pro = profits[i]

        return max_pro
