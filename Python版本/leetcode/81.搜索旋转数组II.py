
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        len_n = len(nums)

        k = 0
        for i in range(1, len_n):
            if nums[i] < nums[i-1]:
                k = i
                break

        if target >= nums[k] and target <= nums[-1]:
            left, right = k, len_n - 1
        else:
            left, right = 0, k - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return False
