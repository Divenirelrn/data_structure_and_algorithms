
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        len_s = len(s)
        if s == " ":
            return 0

        i = len_s - 1
        while i >= 0 and s[i] == " ":
            len_s -= 1
            i -= 1

        ans = 0
        for i in range(len_s - 1, -1, -1):
            if s[i] == " ":
                break

            ans += 1

        return ans