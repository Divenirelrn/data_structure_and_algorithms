class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        len_n = len(nums)
        if len_n <= 2:
            return len_n

        slow = fast = 1
        count = 1
        while fast < len_n:
            if nums[fast] == nums[fast - 1]:
                count += 1
            else:
                count = 1

            if count <= 2:
                nums[slow] = nums[fast]
                slow += 1

            fast += 1

        return slow