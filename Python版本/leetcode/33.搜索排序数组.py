
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        len_nums = len(nums)
        k = 0
        while k < len_nums - 1 and nums[k] < nums[k+1]:
            k += 1

        if target >= nums[0]:
            left, right = 0, k
        else:
            left, right = k + 1, len_nums - 1

        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid] :
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return -1
