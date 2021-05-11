
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_h = len(haystack)
        len_n = len(needle)

        if len_n == 0:
            return 0

        if len_h == 0:
            return -1

        def get_next():
            next_arr = [None] * len_n
            next_arr[0] = -1

            i = 0
            j = -1
            while i < len_n - 1:
                if j == -1 or needle[i] == needle[j]:
                    i += 1
                    j += 1
                    next_arr[i] = j
                else:
                    j = next_arr[j]

            return next_arr

        next_arr = get_next()
        i = j = 0
        while i < len_h and j < len_n:
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = next_arr[j]

        if j == len_n:
            return i - j
        else:
            return -1