class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_n = len(nums)

        slow = fast = 0
        while fast < len_n:
            if nums[fast] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1

            fast += 1

        fast = slow
        while fast < len_n:
            if nums[fast] == 1:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1

            fast += 1


