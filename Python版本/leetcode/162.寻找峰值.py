class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        if n == 2:
            return 0 if nums[0] > nums[1] else 1

        for i in range(n):
            if i == 0 and nums[0] > nums[1]:
                return 0

            if i == n - 1 and nums[n-1] > nums[n-2]:
                return n - 1

            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i