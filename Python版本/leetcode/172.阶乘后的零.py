
class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0

        for i in range(5, n+1, 5):
            j = i
            while j % 5 == 0:
                ans += 1
                j /= 5

        return ans