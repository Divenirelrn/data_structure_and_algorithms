
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = dict()
        len_nums = len(nums)
        for i in range(len_nums):
            if hash.get(nums[i], -1) != -1:
                return [i, hash[nums[i]]]
            else:
                hash[target - nums[i]] = i