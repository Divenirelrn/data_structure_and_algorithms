
import sys

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)

        len_nums = len(nums)
        res = sys.maxsize
        i_value = None
        for i in range(len_nums - 2):
            if nums[i] == i_value:
                continue
            i_value = nums[i]

            l = i + 1
            r = len_nums - 1

            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == target:
                    return target
                elif s < target:
                    l += 1
                    while l < len_nums and nums[i] == nums[i-1]:
                        l += 1
                else:
                    r -= 1
                    while r >= 0 and nums[r] == nums[r+1]:
                        r -= 1

                if abs(s-target) < abs(res-target):
                        res = s

        return res