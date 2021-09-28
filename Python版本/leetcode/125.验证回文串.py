class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        if n == 0:
            return True

        fir, last = 0, n-1
        while fir < last:
            if not s[fir].isalnum():
                fir += 1
                continue

            if not s[last].isalnum():
                last -= 1
                continue

            if s[fir].lower() != s[last].lower():
                return False

            fir += 1
            last -= 1

        return True