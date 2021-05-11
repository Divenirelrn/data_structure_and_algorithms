
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        len_nums = len(nums)
        if len_nums == 0:
            return 0

        if len_nums == 1:
            return 1


        slow = 1
        while slow < len_nums and nums[slow] != nums[slow - 1]:
            slow += 1

        if slow == len_nums:
            return len_nums
        else:
            fast = slow + 1

        while slow < len_nums and fast < len_nums:
            flag = 0
            while fast < len_nums and nums[fast] == nums[fast - 1]:
                fast += 1

            if fast >= len_nums:
                break

            nums[slow] = nums[fast]
            slow += 1
            fast += 1

        return slow