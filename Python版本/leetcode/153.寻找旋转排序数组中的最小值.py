class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        i = 1
        while i < n and nums[i] > nums[i-1]:
            i += 1

        if i < n:
            return nums[i]
        else:
            return nums[0]