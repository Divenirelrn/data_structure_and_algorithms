
#方法一：动态规划+优化
class Solution:
    def canJump(self, nums):
        if 0 not in nums:
            return True

        len_nums = len(nums)
        dp = [False] * len_nums
        dp[0] = True

        pre = 0
        for i in range(1, len_nums):
            for j in range(pre, i):
                if dp[j] and nums[j] >= i - j:
                    dp[i] = True
                    pre = j
                    break

        return dp[-1]

#方法二：贪心算法
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if 0 not in nums:
            return True

        len_nums = len(nums)
        max_dis = 0
        for i in range(len_nums):
            if i <= max_dis:
                max_dis = (i + nums[i]) if (i + nums[i]) > max_dis else max_dis

                if max_dis >= len_nums - 1:
                    return True
            else:
                return False


if __name__ == "__main__":
    s = Solution()
    s.canJump([3,2,1,0,4])