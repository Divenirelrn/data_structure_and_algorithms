class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        n = len(columnTitle)
        base = 1

        for i in range(n-1, -1, -1):
            res += base * (ord(columnTitle[i]) - 64)
            base *= 26

        return res