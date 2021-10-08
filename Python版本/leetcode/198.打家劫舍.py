
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [0] * n
        dp[0] = (nums[0], 0)

        for i in range(1, n):
            temp1 = dp[i - 1][1] + nums[i]
            temp2 = max(dp[i-1][0], dp[i-1][1])

            dp[i] = (temp1, temp2)

        return max(dp[-1][0], dp[-1][1])