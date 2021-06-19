class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        len_nums = len(nums)
        if len_nums <= 1:
            return len_nums

        slow = fast = 1

        while fast < len_nums:
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1

            fast += 1

        return slow