#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 解码
# @param nums string字符串 数字串
# @return int整型
#
class Solution:
    def solve(self, nums: str) -> int:
        # write code here
        if nums[0] == '0':
            return 0
        n = len(nums)
        if n == 1:
            return 1
        dp = [0] * n
        dp[0] = 1
        if nums[1] == '0':
            if nums[0] == '1' or nums[0] == '2':
                dp[1] = 1
            else:
                dp[1] = 0
        else:
            dp[1] = 2 if nums[0] + nums[1] <= '26' else 1
        for i in range(2, n):
            if nums[i] == '0':
                if nums[i - 1] == '1' or nums[i - 1] == '2':
                    dp[i] = dp[i - 2]
                else:
                    dp[i] = 0
            else:
                if nums[i - 1] + nums[i] <= '26' and nums[i - 1] != '0':
                    dp[i] = dp[i - 1] + dp[i - 2]
                else:
                    dp[i] = dp[i - 1]

        return dp[-1]