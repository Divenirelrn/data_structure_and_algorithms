
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        if len(nums) == 0:
            return 0

        len_nums = len(nums)
        i, last = 0, len_nums - 1
        while last >= i and nums[last] == val:
            last -= 1

        while i <= last:
            if nums[i] == val:
                swap(i, last)
                i += 1
                last -= 1
                while last >= i and nums[last] == val:
                    last -= 1
            else:
                i += 1

        return last + 1

