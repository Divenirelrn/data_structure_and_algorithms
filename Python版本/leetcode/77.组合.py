
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n == k:
            return [[i for i in range(1, n+1)]]

        if k == 1:
            return [[i] for i in range(1, n+1)]

        def inner(idx):
            if len(s) == k:
                ans.append(s[:])
                return

            if idx == n + 1:
                return

            for i in range(idx, n+1):
                s.append(i)
                inner(i + 1)
                s.pop()

        s = []
        ans = []
        inner(1)

        return ans