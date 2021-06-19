
#双指针
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

#三指针
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_n = len(nums)
        if len_n == 1:
            return

        p0 = p1 = p = 0
        while p < len_n:
            if nums[p] == 1:
                nums[p1], nums[p] = nums[p], nums[p1]
                p1 += 1
            elif nums[p] == 0:
                nums[p0], nums[p] = nums[p], nums[p0]
                if p0 < p1:
                    nums[p1], nums[p] = nums[p], nums[p1]
                p0 += 1
                p1 += 1

            p += 1






