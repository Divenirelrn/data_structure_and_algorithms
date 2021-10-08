class Solution:
    def hammingWeight(self, n: int) -> int:
        nums = list(str(bin(n))[2:])
        nums = [int(i) for i in nums]

        return sum(nums)