
#方法一：动态规划
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        len_nums = len(nums)
        if len_nums == 1:
            return nums[0]

        max_sum = nums[0]
        dp = [0] * len_nums
        dp[0] = nums[0]
        for i in range(1, len_nums):
            dp[i] = max(nums[i], dp[i-1] + nums[i])

            if dp[i] > max_sum:
                max_sum = dp[i]

        return max_sum

#方法二：分治（仅作为线段树的引入，在本题中并不推荐使用）
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        len_nums = len(nums)
        if len_nums == 1:
            return nums[0]

        def pushup(lres, rres):
            #isum, lsum, rsum, msum
            isum = lres[0] + rres[0]
            lsum = max(lres[1], lres[0] + rres[1])
            rsum = max(rres[2], rres[0] + lres[2])
            msum = max(max(lres[3], rres[3]), lres[2] + rres[1])

            return isum, lsum, rsum, msum

        def inner(left, right):
            if left == right:
                return nums[left], nums[left], nums[left], nums[left]

            mid = (left + right) // 2
            lres = inner(left, mid)
            rres = inner(mid + 1, right)

            return pushup(lres, rres)

        return inner(0, len_nums - 1)[-1]