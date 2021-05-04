
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums = sorted(nums)

        if nums[0] > 0 or nums[-1] < 0:
            return []

        len_nums = len(nums)
        res = []
        i_value = None
        for i in range(len_nums - 2):
            if nums[i] > 0:
                break

            if nums[i] == i_value:
                continue
            i_value = nums[i]

            l = i + 1
            r = len_nums - 1

            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < len_nums and nums[i] == nums[i - 1]:
                        l += 1
                    r -= 1
                    while r >= 0 and nums[r] == nums[r + 1]:
                        r -= 1
                elif s < 0:
                    l += 1
                    while l < len_nums and nums[i] == nums[i - 1]:
                        l += 1
                else:
                    r -= 1
                    while r >= 0 and nums[r] == nums[r + 1]:
                        r -= 1

        return res