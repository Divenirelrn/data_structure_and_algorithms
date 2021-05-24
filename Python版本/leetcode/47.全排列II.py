
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        len_n = len(nums)
        if len_n == 1:
            return [nums]

        hash_t = {}
        for num in nums:
            if num not in hash_t:
                hash_t[num] = 1
            else:
                hash_t[num] += 1

        keys = list(hash_t.keys())

        s = []
        for num in keys:
            s.append([num])
        ans = []
        while len(s):
            rank = s.pop()
            for num in keys:
                count = rank.count(num)

                if count == 0 or count < hash_t[num]:
                    rank.append(num)

                    if len(rank) == len_n:
                        ans.append(rank[:])
                    else:
                        s.append(rank[:])

                    rank.pop()

        return ans