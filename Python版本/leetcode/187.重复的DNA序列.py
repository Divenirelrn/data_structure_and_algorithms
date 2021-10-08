class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n, L = len(s), 10
        if n <= L:
            return []

        hash_map = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        nums = [hash_map[s[i]] for i in range(n)]

        seen = set()
        ans = set()
        h0 = 0
        base, mul = 4, 1
        for i in range(n - L + 1):
            if i > 0:
                h0 = base * h0 - nums[i - 1] * mul + nums[i + L - 1]
            else:
                for l in nums[i:L][::-1]:
                    h0 += l * mul
                    mul *= base

            if h0 in seen:
                ans.add(s[i:i + L])
            else:
                seen.add(h0)

        return list(ans)

