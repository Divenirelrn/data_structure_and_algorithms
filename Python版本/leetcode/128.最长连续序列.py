
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)

        max_len = 0
        num_set = set(nums)
        for num in num_set:
            delta = 1
            if num - 1 not in num_set:
                cur_len = 1

                while num + delta in num_set:
                    cur_len += 1
                    delta += 1

                max_len = max(max_len, cur_len)

        return max_len