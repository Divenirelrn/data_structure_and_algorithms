
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums = sorted(nums)

        res = []
        len_nums = len(nums)

        if target > 0 and nums[len_nums - 1] < 0:
            return []

        fir_v = None
        for i in range(len_nums - 3):
            if target < 0 and nums[i] > 0:
                break

            if nums[i] == fir_v:
                continue
            fir_v = nums[i]

            sec_v = None
            for j in range(i+1, len_nums - 2):
                if nums[j] == sec_v:
                    continue
                sec_v = nums[j]

                left = j + 1
                right = len_nums - 1
                while left < right:
                    s = nums[i] + nums[j] + nums[left] + nums[right]
                    if s == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        while left < len_nums and nums[left] == nums[left-1]:
                            left += 1

                        right -= 1
                        while right >= 0 and nums[right] == nums[right + 1]:
                            right -= 1
                    elif s < target:
                        left += 1
                        while left < len_nums and nums[left] == nums[left-1]:
                            left += 1
                    else:
                        right -= 1
                        while right >= 0 and nums[right] == nums[right + 1]:
                            right -= 1

        return res

