class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def f(x, y):
            sx, sy = 10, 10
            while sx <= x:
                sx *= 10

            while sy <= y:
                sy *= 10

            if sy * x + y >= sx * y + x:
                return -1
            else:
                return 1

        nums = sorted(nums, key=functools.cmp_to_key(f))

        if nums[0] == 0:
            return "0"

        ans = ""
        for num in nums:
            ans += str(num)

        return ans