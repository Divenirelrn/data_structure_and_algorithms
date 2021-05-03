
import math

class Solution:
    def myAtoi(self, s: str) -> int:
        if s == "":
            return 0

        MAX_VALUE = int(math.pow(2,31) - 1)
        MIN_VALUE = int(-math.pow(2, 31))

        len_s = len(s)
        res = ""
        flag = 1
        i = 0
        while i < len_s and s[i] == " ":
            i += 1

        if i >= len_s:
            return 0
        elif s[i] == '-':
            flag = -1
        elif s[i] == '+':
            flag = 1
        elif ord(s[i]) < 48 or ord(s[i]) > 65:
            return 0
        else:
            res += s[i]

        i += 1
        while(i < len_s):
            if ord(s[i]) >= 48 and ord(s[i]) <= 65:
                res += s[i]
            else:
                break

            i += 1

        if len(res) == 0:
            return 0
        else:
            res = int(res)
            if flag == 1:
                return res if res <= MAX_VALUE else MAX_VALUE
            else:
                return -res if -res >= MIN_VALUE else MIN_VALUE