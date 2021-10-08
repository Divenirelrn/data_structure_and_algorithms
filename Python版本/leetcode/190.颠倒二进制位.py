class Solution:
    def reverseBits(self, n: int) -> int:
        nb = str(bin(n))[2:]
        nb = '0' * (32 - len(nb)) + nb

        return int(nb[::-1], 2)