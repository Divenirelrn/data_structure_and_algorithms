
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        len_n = len(nums)

        def inner(idx):
            ans.append(s[:])

            if idx == len_n:
                return

            for i in range(idx, len_n):
                s.append(nums[i])
                inner(i + 1)
                s.pop()

        s = []
        ans = []
        inner(0)

        return ans