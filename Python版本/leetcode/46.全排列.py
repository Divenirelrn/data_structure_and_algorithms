
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        len_n = len(nums)
        if len_n == 1:
            return [nums]

        s = []
        for num in nums:
            s.append([num])
        ans = []
        while len(s):
            rank = s.pop()
            for num in nums:
                if num not in rank:
                    rank.append(num)

                    if len(rank) == len_n:
                        ans.append(rank[:])
                    else:
                        s.append(rank[:])

                    rank.pop()

        return ans