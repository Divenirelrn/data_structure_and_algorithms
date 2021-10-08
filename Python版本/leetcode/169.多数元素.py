
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)

        slow, fast = 0, 0
        while fast < n:
            if nums[fast] == nums[slow]:
                fast += 1
            else:
                if fast - slow > n // 2:
                    return nums[slow]

                slow = fast

        if fast == n and fast - slow > n // 2:
            return nums[slow]