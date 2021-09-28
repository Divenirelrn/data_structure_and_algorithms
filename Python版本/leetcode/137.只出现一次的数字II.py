class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(32):
            s = sum((num >> i) & 1 for num in nums)

            if s % 3:
                if i == 31:
                    ans -= (1 << i)
                else:
                    ans |= (1 << i)

        return ans