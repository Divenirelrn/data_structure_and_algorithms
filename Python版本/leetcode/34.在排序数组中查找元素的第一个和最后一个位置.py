
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        len_nums = len(nums)
        left, right = 0, len_nums - 1
        idx = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                idx = mid
                break
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        if idx == -1:
            return [-1, -1]

        l = r = idx
        while l >= 1 and nums[l-1] == nums[l]:
            l -= 1

        while r < len_nums - 1 and nums[r + 1] == nums[r]:
            r += 1

        return [l, r]