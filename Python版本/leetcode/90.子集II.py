class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        hash_t = {}
        for i in range(len(nums)):
            if hash_t.get(nums[i], -1) != -1:
                hash_t[nums[i]] += 1
            else:
                hash_t[nums[i]] = 1

        nums_new = list(hash_t.keys())
        len_n = len(nums_new)

        def inner(idx):
            ans.append(s[:])

            if idx == len_n:
                return

            for i in range(idx, len_n):
                for j in range(1, hash_t[nums_new[i]] + 1):
                    for _ in range(j):
                        s.append(nums_new[i])
                    inner(i + 1)
                    for _ in range(j):
                        s.pop()

        ans = []
        s = []
        inner(0)

        return ans