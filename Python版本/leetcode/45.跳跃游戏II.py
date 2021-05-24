
class Solution:
    def jump(self, nums: List[int]) -> int:
        len_n = len(nums)
        if len_n == 1:
            return 0
        if len_n == 2:
            return 1

        MAX_VALUE = 65535
        dp = [MAX_VALUE] * len_n
        dp[0] = 0
        dp[1] = 1

        for i in range(2, len_n):
            for j in range(i):
                if nums[j] >= i - j and dp[j] + 1 < dp[i]:
                    dp[i] = dp[j] + 1

        return dp[-1]
